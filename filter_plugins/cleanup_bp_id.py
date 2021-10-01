class FilterModule(object):

    def filters(self):
        return {
            'cleanup_bp_id': self.cleanup_bp_id,
        }

    def cleanup_bp_id(self, value, bp_name):
        for item in value['items']:
            if item["label"] == bp_name:
                return (item["id"])
