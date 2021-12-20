# Secret Key Finder
We can Use this tool to find out sensitive data such as API keys, hardcoded credentials etc.

## Usage
* To find sensitive keys on a target
```
./secret_key_finder.sh https://target.com/
```
* To search for URL in which key is present
```
./key_url_finder.sh <Keyword_Here>
```
  * For Example: 
  ```
  ./key_url_finder.sh "Alzfdvrbrb244566ffdvgbgbt"
  ```

## Installation
```
git clone https://github.com/rsbarsania/secret_key_finder.git
```

```
cd secret_key_finder
```
```
chmod +x *.sh
```
```
./installer.sh
```
##
