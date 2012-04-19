from livesettings import config_register, ConfigurationGroup, PositiveIntegerValue, MultipleStringValue
from django.utils.translation import ugettext_lazy as _

# First, setup a grup to hold all our possible configs
MYAPP_GROUP = ConfigurationGroup(
    'MyApp',               # key: internal name of the group to be created
    _('My App Settings'),  # name: verbose name which can be automatically translated
    ordering=0             # ordering: order of group in the list (default is 1)
)

# Now, add our number of images to display value
# If a user doesn't enter a value, default to 5
config_register(PositiveIntegerValue(
    MYAPP_GROUP,           # group: object of ConfigurationGroup created above
    'NUM_IMAGES',      # key:   internal name of the configuration value to be created
    description = _('Number of images to display'),              # label for the value
    help_text = _("How many images to display on front page."),  # help text
    default = 5        # value used if it have not been modified by the user interface
))

# Another example of allowing the user to select from several values
config_register(MultipleStringValue(
    MYAPP_GROUP,
    'MEASUREMENT_SYSTEM',
    description=_("Measurement System"),
    help_text=_("Default measurement system to use."),
    choices=[('metric',_('Metric')),
        ('imperial',_('Imperial'))],
    default="imperial"
))