import nuke
import nukescripts

from reviewMain import ReviewWindow

# menu = nuke.toolbar('Nodes')
# menu.addCommand('Review', lambda: smartReview.main())

nukescripts.registerWidgetAsPanel('ReviewWindow', "Smart Review", 'uk.co.thefoundry.ReviewWindow', True)