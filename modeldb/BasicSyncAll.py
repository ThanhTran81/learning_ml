from modeldb.basic.ModelDbSyncerBase import *
import yaml

# Create a syncer using a convenience API
syncer_obj = Syncer.create_syncer("Project 2", "test_user", \
    "use sync_all")

# sync_all can use both yaml and json files
# filename = "YamlSample.yaml"
filename = "C:/Users/Tran/git/_learning/learning_ml/data/JsonSample.json"

print "Syncing all data from file..."
syncer_obj.sync_all(filename)

syncer_obj.sync()
