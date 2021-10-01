class FilterModule(object):

    def filters(self):
        return {
            'cleanup_leaf_ids': self.cleanup_leaf_ids,
        }

    def cleanup_leaf_ids(self, value):
        leaf_ids = []
        for k,val in value['nodes'].items():
            if val["role"] == "leaf":
               leaf_ids.append(val["id"])
        return(leaf_ids)
            
