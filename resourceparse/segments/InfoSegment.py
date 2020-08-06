# Copyright (C) Jan 2020 Mellanox Technologies Ltd. All rights reserved.   
#                                                                           
# This software is available to you under a choice of one of two            
# licenses.  You may choose to be licensed under the terms of the GNU       
# General Public License (GPL) Version 2, available from the file           
# COPYING in the main directory of this source tree, or the                 
# OpenIB.org BSD license below:                                             
#                                                                           
#     Redistribution and use in source and binary forms, with or            
#     without modification, are permitted provided that the following       
#     conditions are met:                                                   
#                                                                           
#      - Redistributions of source code must retain the above               
#        copyright notice, this list of conditions and the following        
#        disclaimer.                                                        
#                                                                           
#      - Redistributions in binary form must reproduce the above            
#        copyright notice, this list of conditions and the following        
#        disclaimer in the documentation and/or other materials             
#        provided with the distribution.                                    
#                                                                           
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS       
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN        
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN         
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE          
# SOFTWARE.                                                                 
# --                                                                        


#######################################################
#
# InfoSegment.py
# Python implementation of the Class InfoSegment
# Generated by Enterprise Architect
# Created on:      14-Aug-2019 10:11:57 AM
# Original author: talve
#
#######################################################
from segments.Segment import Segment
from segments.SegmentFactory import SegmentFactory
from utils import constants as cs


class InfoSegment(Segment):
    """this class is responsible for holding info segment data.
    """

    def __init__(self, data):
        """initialize the class by setting the class data.
        """
        super().__init__()
        self.raw_data = data

    def get_data(self):
        """get the general segment data.
        """
        return self.raw_data

    def get_type(self):
        """get the general segment type.
        """
        return cs.RESOURCE_DUMP_SEGMENT_TYPE_INFO

    def get_version(self):
        dw_data = self.get_data()
        # self._parsed_data['Segment Type'] = "{0} ({1})".format("Info Segment",
        #                                                  str(hex(int('{:0b}'.format(dw_data[0]).zfill(32)[16:32], 2))))
        offset = cs.SEGMENTS_HEADER_SIZE_IN_DW
        if len(dw_data) > cs.SEGMENTS_HEADER_SIZE_IN_DW:
        #     self._parsed_data['Dump version'] = str(int('{:0b}'.format(dw_data[offset]).zfill(32)[24:32], 2))
            offset += 1
        #     self._parsed_data['HW version'] = str(int('{:0b}'.format(dw_data[offset]).zfill(32)[0:8], 2)) + "." + str(
        #         int('{:0b}'.format(dw_data[offset]).zfill(32)[8:16], 2)) + "." + str(
        #         int('{:0b}'.format(dw_data[offset]).zfill(32)[16:32], 2))
            offset += 1
            return "{0}.{1}.{2}".format(str(int('{:0b}'.format(dw_data[offset]).zfill(32)[0:8], 2)).rjust(2, '0'),
                                        str(int('{:0b}'.format(dw_data[offset]).zfill(32)[8:16], 2)).rjust(2, '0'),
                                        str(int('{:0b}'.format(dw_data[offset]).zfill(32)[16:32], 2)).rjust(4, '0'))
        return ""

    def add_parsed_data(self, key, value):
        #if key == "fw_version":
        #    self._version_str = "{0}.{1}.{2}".format(str(int('{:0b}'.format(int(value, 16)).zfill(32)[0:8], 2)),
        #                                             str(int('{:0b}'.format(int(value, 16)).zfill(32)[8:16], 2)),
        #                                             str(int('{:0b}'.format(int(value, 16)).zfill(32)[16:32], 2)))
        self._parsed_data[key] = value

    def get_parsed_data(self):
        """get dictionary of parsed segment data.
        """

        # dw_data = self.get_data()
        # self._parsed_data['Segment Type'] = "{0} ({1})".format("Info Segment",
        #                                                  str(hex(int('{:0b}'.format(dw_data[0]).zfill(32)[16:32], 2))))
        # offset = cs.SEGMENTS_HEADER_SIZE_IN_DW
        #
        # if len(dw_data) > cs.SEGMENTS_HEADER_SIZE_IN_DW:
        #     self._parsed_data['Dump version'] = str(int('{:0b}'.format(dw_data[offset]).zfill(32)[24:32], 2))
        #     offset += 1
        #     self._parsed_data['HW version'] = str(int('{:0b}'.format(dw_data[offset]).zfill(32)[0:8], 2)) + "." + str(
        #         int('{:0b}'.format(dw_data[offset]).zfill(32)[8:16], 2)) + "." + str(
        #         int('{:0b}'.format(dw_data[offset]).zfill(32)[16:32], 2))
        #     offset += 1
        #     self._parsed_data['FW version'] = str(int('{:0b}'.format(dw_data[offset]).zfill(32)[0:8], 2)) + "." + str(
        #         int('{:0b}'.format(dw_data[offset]).zfill(32)[8:16], 2)) + "." + str(
        #         int('{:0b}'.format(dw_data[offset]).zfill(32)[16:32], 2))

        return self._parsed_data


SegmentFactory.register(cs.RESOURCE_DUMP_SEGMENT_TYPE_INFO, InfoSegment)