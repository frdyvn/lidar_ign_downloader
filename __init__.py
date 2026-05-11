def classFactory(iface):
    from .lidar_ign_downloader import LidarIgnDownloaderPlugin
    return LidarIgnDownloaderPlugin(iface)