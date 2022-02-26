const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const ytdl = require("ytdl-core");
const app = express();
const fs = require("fs");
const fetch = require("node-fetch")
const FormData = require("form-data")
const { fromBuffer } = require("file-type")

let PORT = process.env.PORT || 8080 || 5000 || 3000


async function upload(buffer) {
  const { ext } = await fromBuffer(buffer)
  let form = new FormData
  form.append("file", buffer, "tmp." + ext)
  let res = await fetch("https://telegra.ph/upload", {
    method: "POST",
    body: form
  })
  let img = await res.json()
  if (img.error) throw img.error
  return "https://telegra.ph" + img[0].src
}

app.listen(PORT, function() {
  console.log("Server is working at port 4000 11");
})

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/download", function(req, res) {
  res.send("Method not allowed!");
})

app.post("/download", async function(req, res) {
  let { url } = req.body;

  let stream = fs.createWriteStream("./result.mp4");

  let result = "";
  let error = false;
  try {
    (await ytdl(url)).pipe(stream);
  } catch(err) {
    console.log(err)
    error = true;
  };

  stream.on("finish", async function() {
    result = await upload(fs.readFileSync("./result.mp4"))
    console.log(fs.readFileSync("./result.mp4"))
    let html = `
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width-device-width, initial-scale=1.0"> <meta http-equiv="X-UA-Compatible" content="ie-edge"> <title>Youtube Downloader</title>
  </head>
  <body>
    <h1 class="heading">Youtube Downloader</h1>
    <p>Status : ${error ? "gagal" : "sukses"}</p>
    <p>Format : video</p>
${!error ? "      <button style=\"border-radius: 8px 4px 4px 0px;border: 2px solid #2485ff;background: #2485ff;color: white;\" onclick=\'location.href = \"" + result + "\"\'>Download</button>" : ""}
  </body>
</html>
`.trim()
    res.send(html)
    fs.unlinkSync("./result.mp4");
  })
});
