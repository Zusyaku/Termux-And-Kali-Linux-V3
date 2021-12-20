from typing import Union
from re import sub

class Texto:

    def __init__(self) -> None:
        pass

    def tsplit(self, text: Union[str]) -> str:
        """
        Get title hentai and delete blablabla
        :text: String
        """
        pattern = r"(?i)(\[yaoi alert\]|\[uncensored\]|\[new release\]|\[batch\]|\[remastered\]|\[fix\]|\[special xmas\]|\[jav sub indo\]|\[tamat\]|\[3d\]|\[3d hentai\]|re-upload)"
        return sub(pattern, "", text).strip()

    def reso(self, text: Union[str]) -> str:
        """
        Get resoluion only
        :text: String
        """
        return text.split("Indonesia")[1].strip(" [").strip("]") if "Indonesia" in text else text.split()[-1].strip("[").strip("]")
