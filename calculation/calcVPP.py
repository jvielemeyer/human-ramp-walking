import numpy as np
import math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from numpy import genfromtxt #to get NaN for empty columns


def VPP_calculation(COP,COPz,COM,Force_x, Force_z,VPP_init,trunk_angle,align,file):
    def f(VPP_init):
        def VPPsum_dist_squared(VPP, xVPP_beg, xVPP_end, zVPP_beg, zVPP_end):

            xVPP_beg = xVPP_beg[~np.isnan(xVPP_beg)]
            xVPP_end = xVPP_end[~np.isnan(xVPP_end)]
            zVPP_beg = zVPP_beg[~np.isnan(zVPP_beg)]
            zVPP_end = zVPP_end[~np.isnan(zVPP_end)]

            r = -((xVPP_beg - xVPP_end) * (xVPP_end - VPP[0]) + (zVPP_beg - zVPP_end) * (zVPP_end - VPP[1])) / \
                ((xVPP_beg - xVPP_end)**2 + (zVPP_beg - zVPP_end)**2)

            Xx = xVPP_end + r * (xVPP_beg - xVPP_end)
            Xz = zVPP_end + r * (zVPP_beg - zVPP_end)

            r_squared = (VPP[0] - Xx)**2 + (VPP[1] - Xz)**2
            y_temp = np.sqrt(r_squared)
            y = np.sum(y_temp)

            return y

        y_VPP_rot = VPPsum_dist_squared(VPP_init, x_beg_rot, x_end_rot, z_beg_rot, z_end_rot)

        return y_VPP_rot

    if 0 in Force_x or 0 in Force_z:
        result =[np.nan,np.nan]
        print("Error at " + file + " in VPP calculation. Wrong TD and TO events?")
        return result

    else:

        if align == 0:
            trunk_angle = np.full([len(COP), 1],0)#vertical aligned
        #else: #align == 1
         #   continue #rotated to trunk-aligned coordinate frame
        COPx_rot = np.full([len(COP), 1], np.nan)
        COPz_rot = np.full([len(COP), 1], np.nan)
        Force_x_rot = np.full([len(COP), 1], np.nan)
        Force_x_rot1 = np.full([len(COP), 1], np.nan)
        Force_z_rot = np.full([len(COP), 1], np.nan)
        for i in range (0,len(COP)):
            COPx_rot[i] = (COP[i]- COM[i,0])*math.cos(math.radians(trunk_angle[i])) + (COPz[i]- COM[i,1])*math.sin(math.radians(trunk_angle[i])) #angle in rad
            COPz_rot[i] = -(COP[i]- COM[i,0])*math.sin(math.radians(trunk_angle[i])) + (COPz[i]- COM[i,1])*math.cos(math.radians(trunk_angle[i]))
            Force_x_rot[i] = Force_x[i]*math.cos(math.radians(trunk_angle[i])) + Force_z[i]*math.sin(math.radians(trunk_angle[i]))
            Force_x_rot1[i] = Force_x[i]*math.cos(math.radians(trunk_angle[i]))
            Force_z_rot[i] = -Force_x[i]*math.sin(math.radians(trunk_angle[i])) + Force_z[i]*math.cos(math.radians(trunk_angle[i]))


        COPx_rot = COPx_rot.reshape(len(COP))
        COPz_rot = COPz_rot.reshape(len(COP))
        Force_x_rot = Force_x_rot.reshape(len(COP))
        Force_z_rot = Force_z_rot.reshape(len(COP))

        x_beg_rot = COPx_rot #Com-centered
        x_end_rot = COPx_rot + Force_x_rot
        z_beg_rot = COPz_rot
        z_end_rot = COPz_rot+ Force_z_rot

        result = minimize(f, VPP_init)
        if 0 in result.x:
            result.x = [np.nan,np.nan]

        return result.x



def R_mod(COP,COPz,COM, Force_x, Force_z, trunk_angle,align, VPP_calc, nmb_force_plate):
    def R_squared(R):
        # calculate explained variation of theoretical and measured forces
        # formula: see Herr and Popovic (2008): Angular momentum in human walking
        temp_mean = np.nanmean(R["theta_exp"])
        t_exp_mean = np.nanmean(temp_mean)

        numerator = np.nansum(np.power(R["theta_exp"] - R["theta_mod"], 2))
        denominator = np.nansum(np.power(R["theta_exp"] - t_exp_mean, 2))

        R_2 = 1 - np.sum(numerator) / np.sum(denominator)
        return R_2
    if ~np.isnan(VPP_calc[0]):
        if align == 0:
            trunk_angle = np.full([len(COP), 1], 0) #vertical aligned
        # else: #align == 1
        #    continue
        Cop_Com_Centered = np.transpose([COP,COPz])- COM

        #----------------initialize
        COPx_rot = np.full([len(COP), 1], np.nan)
        COPz_rot = np.full([len(COP), 1], np.nan)
        Force_x_rot = np.full([len(COP), 1], np.nan)
        Force_z_rot = np.full([len(COP), 1], np.nan)
        for i in range (0,len(COP)):
            COPx_rot[i] = Cop_Com_Centered[i][0]*math.cos(math.radians(trunk_angle[i])) + Cop_Com_Centered[i][1]*math.sin(math.radians(trunk_angle[i]))#angle in rad
            COPz_rot[i] = -Cop_Com_Centered[i][0]*math.sin(math.radians(trunk_angle[i])) + Cop_Com_Centered[i][1]*math.cos(math.radians(trunk_angle[i]))
            Force_x_rot[i] = Force_x[i]*math.cos(math.radians(trunk_angle[i])) + Force_z[i]*math.sin(math.radians(trunk_angle[i]))
            Force_z_rot[i] = -Force_x[i]*math.sin(math.radians(trunk_angle[i])) + Force_z[i]*math.cos(math.radians(trunk_angle[i]))
        COPx_rot = COPx_rot.reshape(len(COP))
        COPz_rot = COPz_rot.reshape(len(COP))
        Force_x_rot = Force_x_rot.reshape(len(COP))
        Force_z_rot = Force_z_rot.reshape(len(COP))
        #------------

        VPP_COP_Centered = VPP_calc - np.transpose([COPx_rot,COPz_rot])
        VPP_Angle = np.squeeze(np.arctan2(VPP_COP_Centered[:, 1], VPP_COP_Centered[:, 0]))
        VPP_Angle[VPP_Angle < 0] = VPP_Angle[VPP_Angle < 0] + np.pi
        Force_Angle = np.squeeze(np.arctan2(Force_z, Force_x))
        Force_Angle[Force_Angle < 0] = Force_Angle[Force_Angle < 0] + np.pi

        R_calc_ss1 = {
            'theta_mod': VPP_Angle,
            'theta_exp': Force_Angle
        }

        r_mod = R_squared(R_calc_ss1)
    else:
        r_mod = np.nan

    return r_mod



