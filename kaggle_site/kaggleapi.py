import os
import zipfile
import kaggle


def fetch_dataset(url, savefolder):
    """Fetches kaggle competion dataset and saves in desired location.

    Arguments:
        url {str} -- url of kaggle competion.
        savefolder {str} -- path to save dataset
    """

    url_path = '/'.join(url.split('/')[-2:])
    kaggle.api.dataset_download_files(url_path, path=savefolder)
    for f in os.listdir(savefolder):
        if '.zip' in f:
            with open(savefolder + '/' + f, 'rb') as fi:
                zf = zipfile.ZipFile(fi)
                zf.extractall(savefolder)
                os.remove(savefolder + '/' + f)
