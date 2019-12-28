# nutrition

[![CircleCI](https://circleci.com/gh/erikdeirdre/nutrition.svg?style=svg)](https://circleci.com/gh/erikdeirdre/nutrition)
[![Coverage Status](https://coveralls.io/repos/github/erikdeirdre/nutrition/badge.svg?branch=)](https://coveralls.io/github/erikdeirdre/nutrition?branch=)
[![codecov](https://codecov.io/gh/erikdeirdre/nutrition/branch/master/graph/badge.svg)](https://codecov.io/gh/erikdeirdre/nutrition)

This is my attempt at learning more `Flask` and `Angular` by creating a recipe system which includes nutrition ability. 

Let's see how far I get with this.

### Troubleshooting

#### Problem
If executing `flask initdb` results in:
```bash
Usage: flask [OPTIONS] COMMAND [ARGS]...
Try "Flask --help" for help.

Error: No such command "initdb".
```

#### Solution
Make sure `FLASK_APP` variable is set to 'nutrition.py'
