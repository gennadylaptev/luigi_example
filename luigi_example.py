import luigi
from luigi import Task, Parameter, LocalTarget


class CollectMetaInfo(Task):
    """ Given a file with youtube videos URLs, get their metainfo 
        and stores it in the local file system
    """


class FilterVideos(Task):
    """ Given youtube videos metainfo, filter videos for downloading """


class VideoDownloader(Task):
    """ Given a list of videos, download them to the local machine """


class Starter(Task):
    
    # define dependencies
    def requires(self):
        return []

    # define the result of this task
    def output(self):
        pass
    
    # define main logic
    def run(self):
        pass



