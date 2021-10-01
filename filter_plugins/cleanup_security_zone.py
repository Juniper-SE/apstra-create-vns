class FilterModule(object):

    def filters(self):
        return {
            'cleanup_security_zone': self.cleanup_security_zone,
        }

    def cleanup_security_zone(self, value, sz_name):
        for k,val in value['nodes'].items():
            if val["vrf_name"] == sz_name:
               return (val["id"])
            
