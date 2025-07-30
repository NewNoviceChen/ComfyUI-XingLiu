from .nodes.text2image import Text2ImageNode
from .nodes.makeHiResFix import MakeHiResFixNode
from .nodes.makeLora import MakeLoraNode, MergeLoraNode
from .nodes.auth import MakeAuthNode
from .nodes.image2image import Image2ImageNode
from .nodes.makeControlNet import MakeControlNetNode, MergeControlNetNode
from .nodes.uploadLibLib import UploadLibLibNode

NODE_CLASS_MAPPINGS = {
    "MakeAuth": MakeAuthNode,
    "MakeControlNet": MakeControlNetNode,
    "MergeControlNet": MergeControlNetNode,
    "Image2Image": Image2ImageNode,
    "UploadLibLib": UploadLibLibNode,
    "MakeLora": MakeLoraNode,
    "MergeLora": MergeLoraNode,
    "MakeHiResFix": MakeHiResFixNode,
    "Text2Image": Text2ImageNode,

}
