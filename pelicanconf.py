AUTHOR = 'Alin Morosanu'
SITENAME = 'Design Patterns in Python'
SITE_URL = "http://design-patterns-python.morosanu.co.uk"
THEME = 'mytheme'

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
INDEX_SAVE_AS = 'index.html'
DISPLAY_PAGES_ON_MENU = False # Disable automatic page menu items
DISPLAY_CATEGORIES_ON_MENU = False # Assuming you don't want categories in the menu either
MENUITEMS = (
    ('Home', '/'),
    ('About', '/about.html'),
    ('Contact', '/contact.html'),
    # Add other pages you want in the menu here
)
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_PATHS = ['pages', 'projects']
# Sidebar settings
DISPLAY_CATEGORIES_ON_SIDEBAR = False
# DISPLAY_TAGS_ON_SIDEBAR = True # Keep tags if desired
# SOCIAL = (('GitHub', 'https://github.com/your-username'),) # Example social link
# LINKS = (('Pelican', 'https://getpelican.com/'),) # Example link
