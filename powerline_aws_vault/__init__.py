from powerline import PowerlineLogger
from powerline.theme import requires_segment_info


@requires_segment_info
def aws_vault_profile(pl: PowerlineLogger, segment_info: dict) -> str:
    profile = str(segment_info['environ'].get('AWS_VAULT', '@'))
    return profile or '@'
