# -*- coding: utf-8 -*-
"""
downloads East North Vertical nevada reno position files
IGS2014 frame
author: kristine larson
"""
import argparse
import wget
import sys
import os


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("station", help="station name", type=str)
    args = parser.parse_args().__dict__

    # only return a dictionary of arguments that were added from the user - all other defaults will be set in code below
    return {key: value for key, value in args.items() if value is not None}


def download_unr(station: str):
    """
        Command line interface for download_blewitt
        Parameters:
        ___________
        station : string
            4 character ID of the station
    """

    if len(station) != 4:
        print('illegal station name-must be 4 characters')
        sys.exit()
    # geoff blewitt likes upper case
    station = station.upper()
    url= 'http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/'
    fname = station + '.tenv3'
    stationL = station.lower() # lower case
    url = url + fname
    # file will be stored here
    myfname = stationL + '_igs14.tenv3'
    try:
        wget.download(url, out=myfname)
    except:
        print('\n download failed:', url)

    if os.path.exists(fname):
        print('\n SUCCESS:', myfname)


def main():
    args = parse_arguments()
    download_unr(**args)


if __name__ == "__main__":
    main()
