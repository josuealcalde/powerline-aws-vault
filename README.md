# Powerline-aws-vault
This is the [Powerline](https://github.com/powerline/powerline) segment to show current [aws-vault](https://github.com/99designs/aws-vault) profile , soy you are less like to make a deadly mistake.

Tested with BASH.

## Installation

Firstly, install the package locally.
```
git clone https://github.com/josuealcalde/powerline-aws-vault.git

cd powerline-aws-vault

python3 setup.py install --user
```

Then add the colorscheme in the `~/.config/powerline/colorschemes/default.json`

```json
        (...)
        "aws_vault_profile": { "fg": "white", "bg": "darkcyan", "attrs": [] }
    }
}
```

Finally add the segment to your powerline shell config in `~/.config/powerline/themes/shell/default.json`.

```json
{
    "segments": {
        "left": [
            (...)
            {
                "function": "powerline_aws_vault.aws_vault_profile",
                "priority": 10
            }
        ],
        "right": []
    }
}
```
Then you can restart the powerline daemon by:

```
powerline-daemon -k
```

and check if the segment works in a BASH terminal that has AWS session (namely the `$AWS_PROFILE` environment variable).