
from controllers import *
route = [
                (
                        r"/",
                        home.homeHandler
                ),
                (
                                r"/pnr",
                                pnrController.pnrHandler
                )
]
