from .nodes.kling2Video import Text2VideoKlingNode, Image2VideoKlingNode
from .nodes.makeImageList import MergeImageListNode
from .nodes.text2image import Text2ImageCustomNode, Text2ImageByAlphaNode, Text2ImageCustomAlphaNode, \
    Text2ImageF1ContentNode
from .nodes.makeHiResFix import MakeHiResFixNode
from .nodes.makeLora import MakeLoraNode, MergeLoraNode
from .nodes.auth import MakeAuthNode
from .nodes.image2image import Image2ImageByAlphaNode, Image2ImageCustomNode, Image2ImageCustomAlphaNode, \
    Image2ImageF1ContentNode
from .nodes.makeControlNet import MakeControlNetNode, MergeControlNetNode
from .nodes.uploadLibLib import UploadLibLibNode

NODE_CLASS_MAPPINGS = {
    "MakeAuth": MakeAuthNode,
    "MakeControlNet": MakeControlNetNode,
    "MergeControlNet": MergeControlNetNode,
    "Image2ImageByAlpha": Image2ImageByAlphaNode,
    "Image2ImageCustom": Image2ImageCustomNode,
    "UploadLibLib": UploadLibLibNode,
    "MakeLora": MakeLoraNode,
    "MergeLora": MergeLoraNode,
    "MakeHiResFix": MakeHiResFixNode,
    "Text2ImageCustom": Text2ImageCustomNode,
    "Text2ImageByAlpha": Text2ImageByAlphaNode,
    "Text2ImageCustomAlpha": Text2ImageCustomAlphaNode,
    "Image2ImageCustomAlpha": Image2ImageCustomAlphaNode,
    "Text2ImageF1ContentNode": Text2ImageF1ContentNode,
    "Image2ImageF1ContentNode": Image2ImageF1ContentNode,
    "MergeImageListNode": MergeImageListNode,
    "Text2VideoKlingNode": Text2VideoKlingNode,
    "Image2VideoKlingNode(can`t use)": Image2VideoKlingNode
}
