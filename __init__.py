from .nodes.text2image import Text2ImageCustomNode, Text2ImageByAlphaNode, Text2ImageCustomAlphaNode
from .nodes.makeHiResFix import MakeHiResFixNode
from .nodes.makeLora import MakeLoraNode, MergeLoraNode
from .nodes.auth import MakeAuthNode
from .nodes.image2image import Image2ImageByAlphaNode, Image2ImageCustomNode, Image2ImageCustomAlphaNode
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
    "Image2ImageCustomAlpha": Image2ImageCustomAlphaNode

}
