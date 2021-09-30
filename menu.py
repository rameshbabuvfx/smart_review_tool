import nuke

import smartReview

menu = nuke.toolbar('Nodes')
menu.addCommand('Review', lambda: smartReview.main())
