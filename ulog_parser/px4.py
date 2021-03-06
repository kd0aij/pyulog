
from __future__ import print_function

__author__  = "Beat Kueng"

class PX4ULog:
    """
    This class contains PX4-specific ULog things (field names, etc.)
    """

    def __init__(self, ulog_object):
        """
        @param ulog_object: ULog instance
        """
        self.ulog = ulog_object


    def get_mav_type(self):
        """ return the MAV type as string from initial parameters """

        if 'MAV_TYPE' in self.ulog.initial_parameters:
            mav_type = self.ulog.initial_parameters['MAV_TYPE']
            if (mav_type == 1): return 'Fixed Wing'
            if (mav_type == 2): return 'Multirotor'
            if (mav_type == 20): return 'VTOL Tailsitter'
            if (mav_type == 21): return 'VTOL Tiltrotor'
            if (mav_type == 22): return 'VTOL Standard'
        return 'unknown type'


    def get_estimator(self):
        """ return the configured estimator as string from initial parameters """

        if 'SYS_MC_EST_GROUP' in self.ulog.initial_parameters:
            mav_type = self.ulog.initial_parameters['SYS_MC_EST_GROUP']
            if (mav_type == 0): return 'INAV'
            if (mav_type == 1): return 'LPE'
            if (mav_type == 2): return 'EKF2'
        return 'unknown'



