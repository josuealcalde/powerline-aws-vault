from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

@requires_segment_info
class AWSVaultSegment(Segment):
  divider_highlight_group = None

  def __call__(self, pl, segment_info, create_watcher=None):
    profile = segment_info['environ'].get('AWS_VAULT')
    if profile:
        return [{'contents': f'\U00002601  {profile}', 'highlight_groups': ['aws_vault_profile']}]
    return

aws_vault_profile = with_docstring(AWSVaultSegment(), '''Return the AWS Vault profile.''')
