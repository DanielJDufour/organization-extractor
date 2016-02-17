# organization-extractor
organization-extractor helps you extract organizations from text

# Installation
```
pip install organization-extractor
```

# Use
```
from organization_extractor import extract_organizations
text = "I attended the University of Mars and the University of Pluto"
organizations = extract_organizations(text)
print organizations
# prints ["University of Mars", "University of Pluto"]
```

# Features
| Languages Supported |
| ------------------- |
| Arabic |
| English |

# Testing
To test the package run
```
python -m unittest organization_extractor.tests.test
