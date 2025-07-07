import matplotlib.pyplot as plt
import psychrolib
import chart
import argparse
import json

class PassiveDesignConsultant:
    def __init__(self, dbt=None, rh=None, elevation=0):
        self.dbt = dbt if dbt is not None else []
        self.rh = rh if rh is not None else []
        self.elevation = elevation
        self.fig = plt.figure()

    def psychrometric_graph(self, text = "0 - 0.5 m/s", comf = 1, epw = 1, evap = 1, thm = 1, sun = 1, custom_dbt = 0, custom_rh = 0, custom_count_psycho = 8760, evap_efficiency = 80 ):
        dbt = self.dbt
        rh = self.rh
        if custom_dbt == 0 and custom_rh == 0:
            custom_dbt = self.dbt
            custom_rh = self.rh
        psychrolib.SetUnitSystem(psychrolib.SI)
        altitude = self.elevation
        tem = [0, 50]
        hum = [0, 32]
        p = psychrolib.GetStandardAtmPressure(altitude)
        w = [psychrolib.GetHumRatioFromRelHum(i, j / 100, p) for i, j in zip(custom_dbt, custom_rh)]

        if text == "0 - 0.5 m/s":
            a = psychrolib.GetTWetBulbFromRelHum(28.5, .8, p)
            b = 100 * psychrolib.GetRelHumFromTWetBulb(50, a, p)
            c = [psychrolib.GetHumRatioFromRelHum(28.5, .8, p), psychrolib.GetHumRatioFromRelHum(18, .2, p)]
            points = [18, 28.5, 80, 80, 18, 32, 20, 20, 18, 18, 20, 80, 32, 32, 20, 50, 28.5, 80, 32, 50, 28.5, 80, 34,
                      58.51, 18, 20, 37.4, 6.43, 28.5, 80, 50, b, 18, 20, 24.64, 0, 28.5, 80, 39.587, 43.129, 39.587, 8.433, 24.34, 20, 698.324, 42.952, 2271.766, 75.516, 0.020256, 0.002610, 188.574, 37.902]

        if text == "0.5 - 1.0 m/s":
            a = psychrolib.GetTWetBulbFromRelHum(30, .8, p)
            b = 100 * psychrolib.GetRelHumFromTWetBulb(50, a, p)
            c = [psychrolib.GetHumRatioFromRelHum(30, .8, p), psychrolib.GetHumRatioFromRelHum(18, .2, p)]
            points = [18, 30, 80, 80, 18, 33, 20, 20, 18, 18, 20, 80, 33, 33, 20, 50, 30, 80, 33, 50, 30, 80, 36.5,
                      55.57, 18, 20, 39.9, 5.62, 30, 80, 50, b, 18, 20, 24.64, 0, 30, 80, 39.862, 46.344, 39.862, 8.310, 24.34, 20, 498.421, 41.2822, 2240.896, 80.7249, 0.022154, 0.002610, 170.255, 36.953]

        if text == "1.0 - 1.5 m/s":
            a = psychrolib.GetTWetBulbFromRelHum(31, .8, p)
            b = 100 * psychrolib.GetRelHumFromTWetBulb(50, a, p)
            c = [psychrolib.GetHumRatioFromRelHum(31, .8, p), psychrolib.GetHumRatioFromRelHum(18, .2, p)]
            points = [18, 31, 80, 80, 18, 34.5, 20, 20, 18, 18, 20, 80, 34.5, 34.5, 20, 50, 31, 80, 34.5, 50, 31, 80,
                      36.5, 58.84, 18, 20, 39.9, 5.62, 31, 80, 50, b, 18, 20, 24.64, 0, 31, 80, 40.212, 48.165, 40.212, 8.156, 24.34, 20, 592.316, 45.227, 2218.0714, 84.278, 0.023507, 0.002610, 159.22, 40.744]

        count = [0, 0, 0, 0]
        for tem_dbt, rehum, humratio in zip(custom_dbt, custom_rh, w):
            ## for evaporative cooler efficiency ##
            comfort_through_evap_cooler = 0
            if evap_efficiency < 100 and evap_efficiency > 0:
                tem_wbt = psychrolib.GetTWetBulbFromRelHum(tem_dbt, rehum/100, p)
                dbt_out_evap_cooler = tem_dbt - (evap_efficiency/100)*(tem_dbt - tem_wbt)
                rh_out_evap_cooler = 100*psychrolib.GetRelHumFromTWetBulb(dbt_out_evap_cooler, tem_wbt, p)
                hum_ratio_out_evap_cooler = psychrolib.GetHumRatioFromRelHum(dbt_out_evap_cooler, round(rh_out_evap_cooler/100, 2), p)
                #print(tem_dbt, rehum, dbt_out_evap_cooler, rh_out_evap_cooler)
                if dbt_out_evap_cooler <= points[5] and rh_out_evap_cooler >= 20 and hum_ratio_out_evap_cooler < ((points[45] - dbt_out_evap_cooler) / points[44]):
                    comfort_through_evap_cooler = 1
            if evap_efficiency == 100:
                comfort_through_evap_cooler = 1
            

            ##counting hours for every zone ###
            if comf == 1 and tem_dbt >= 18 and tem_dbt <= points[5] and rehum >= 20 and rehum <= 80 and humratio < ((points[45] - tem_dbt) / points[44]):
                count[0] = count[0] + 1
            else:
                if evap == 1 and tem_dbt > 18 and rehum < 80 and humratio < ((points[47] - tem_dbt) / points[46]) and humratio > ((24.64 - tem_dbt) / 2490.6226) and comfort_through_evap_cooler == 1:
                    count[1] = count[1] + 1
                if thm == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[48] and humratio > points[49] and humratio < ((points[51] - tem_dbt) / points[50]):
                    count[2] = count[2] + 1
                if sun == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[48] and humratio > 0.003941434281894339 and tem_dbt < points[38]:
                    count[3] = count[3] + 1

        dbt_can_comf = [[],[],[]]
        rh_can_comf = [[],[],[]]
        dbt_out_comf = []
        rh_out_comf = []
        dbt_comf = []
        rh_comf = []

        c = [0, 0, 0, 0, 0]
        for tem_dbt, rehum, humratio in zip(custom_dbt, custom_rh, w):

            ## for evaporative cooler efficiency ##
            comfort_through_evap_cooler = 0
            if evap_efficiency < 100 and evap_efficiency > 0:
                tem_wbt = psychrolib.GetTWetBulbFromRelHum(tem_dbt, rehum / 100, p)
                dbt_out_evap_cooler = tem_dbt - (evap_efficiency / 100) * (tem_dbt - tem_wbt)
                rh_out_evap_cooler = 100 * psychrolib.GetRelHumFromTWetBulb(dbt_out_evap_cooler, tem_wbt, p)
                hum_ratio_out_evap_cooler = psychrolib.GetHumRatioFromRelHum(dbt_out_evap_cooler,
                                                                             round(rh_out_evap_cooler / 100, 2), p)
                #print(tem_dbt, rehum, dbt_out_evap_cooler, rh_out_evap_cooler)
                if dbt_out_evap_cooler <= points[5] and rh_out_evap_cooler >= 20 and hum_ratio_out_evap_cooler < (
                        (points[45] - dbt_out_evap_cooler) / points[44]):
                    comfort_through_evap_cooler = 1
            if evap_efficiency == 100:
                comfort_through_evap_cooler = 1


            if  tem_dbt >= 18 and tem_dbt <= points[
                5] and rehum >= 20 and rehum <= 80 and humratio < (
                    (points[45] - tem_dbt) / points[44]):
                dbt_comf.append(tem_dbt)
                rh_comf.append(rehum)
                c[0] = c[0] + 1
            else:
                if evap == 1 and tem_dbt > 18 and rehum < 80 and humratio < (
                        (points[47] - tem_dbt) / points[46]) and humratio > ((24.64 - tem_dbt) / 2490.6226) and comfort_through_evap_cooler == 1:
                    dbt_can_comf[0].append(tem_dbt)
                    rh_can_comf[0].append(rehum)
                    c[1] = c[1] + 1
                elif thm == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[48] and humratio > points[
                    49] and humratio < ((points[51] - tem_dbt) / points[50]):
                    dbt_can_comf[1].append(tem_dbt)
                    rh_can_comf[1].append(rehum)
                    c[2] = c[2] + 1
                elif sun == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[
                    48] and humratio > 0.003941434281894339 and tem_dbt < points[38]:
                    dbt_can_comf[2].append(tem_dbt)
                    rh_can_comf[2].append(rehum)
                    c[3] = c[3] + 1
                else:
                    dbt_out_comf.append(tem_dbt)
                    rh_out_comf.append(rehum)
                    c[4] = c[4] + 1
        max_c_value = max(count[1],count[2],count[3])
        max_passive  = ""
        if max_c_value == count[1]:
            max_passive = "Evaporative Cooling"
        if max_c_value == count[2]:
            max_passive = "Thermal Mass"
        if max_c_value == count[3]:
            max_passive = "Sun Shading"

        #self.label_max_passive.setText( "o  " + str(round(((count[0] * 100) / custom_count_psycho), 2)) + "% of hours of outdoor conditions are already comfortable.\n"
        #                                "o  " + str(round(((count[1] * 100) / custom_count_psycho), 2)) +"% of hours can be made comfortable if Evaporative cooling system is used in building.\n"
        #                                "o  " + str(round(((count[2] * 100) / custom_count_psycho), 2)) +"% of hours can be made comfortable if Thermal mass is used in building.\n"
        #                                "o  " + str(round(((count[3] * 100) / custom_count_psycho), 2)) +"% of hours can be made comfortable if Sun shading devices is used in building.\n"
        #                                "o  " + "The possible comfortable hours using the selected passive design strategies is " + str(round((((c[0]+c[1]+c[2]+c[3]) * 100) / custom_count_psycho), 2)) + "%.")
        #self.checkbox_comf.setText("Comfortable Outdoor Conditions (" + str(round(((count[0]*100)/custom_count_psycho), 1)) + "%)")
        #self.checkbox_evap.setText("Evaporative cooling (" + str(round(((count[1] * 100) / custom_count_psycho), 1)) + "%)")
        #self.checkbox_thml.setText("Thermal mass (" + str(round(((count[2] * 100) / custom_count_psycho), 1)) + "%)")
        #self.checkbox_sunshad.setText("Sun shading (" + str(round(((count[3] * 100) / custom_count_psycho))) + "%)")
        #self.checkbox_comf_net.setText("Possible Comfort hours (passive) (" + str(round((((c[0]+c[1]+c[2]+c[3]) * 100) / custom_count_psycho), 1)) + "%)")
        #self.checkbox_active_points.setText("Active Cooling/Heating/Dehum (" + str(round(100 - round((((c[0]+c[1]+c[2]+c[3]) * 100) / custom_count_psycho), 1))) + "%)")
        # Remove GUI code and call psycho_plot directly
        self.psycho_plot(dbt, rh, w, altitude, tem, hum, text, comf, epw, evap, thm, sun, points, dbt_can_comf, rh_can_comf, dbt_out_comf, rh_out_comf, dbt_comf, rh_comf, c)

    def psycho_plot(self, dbt, rh, w, altitude, tem, hum, text, comf, epw, evap, thm, sun, points, dbt_can_comf, rh_can_comf, dbt_out_comf, rh_out_comf, dbt_comf, rh_comf, c):
        self.fig.clear()
        ax8 = self.fig.add_subplot()
        psychrolib.SetUnitSystem(psychrolib.SI)

        custom_style = {
            "figure": {
                #"figsize": [12, 12],
                "base_fontsize": 40,
                "title": "",
                #"title": "PSYCHROMETRIC CHART " + "(Altitude = " + str(altitude) + " m)",
                "x_label": "Dry-bulb temperature, $°C$",
                "y_label": "Humidity ratio $w, g_w / kg_{da}$",
                "x_axis": {"color": [0.2, 0.2, 0.2], "linewidth": 2, "linestyle": "-"},
                "x_axis_labels": {"color": [0.2, 0.2, 0.2], "fontsize": 10},
                "y_axis": {"color": [0.3, 0.3, 0.3], "linewidth": 2, "linestyle": "-"},
                "y_axis_labels": {"color": [0.3, 0.3, 0.3], "fontsize": 10},
                "x_axis_ticks": {"direction": "out", "color": [0.2, 0.2, 0.2]},
                "y_axis_ticks": {"direction": "out", "color": [0.3, 0.3, 0.3]},
                "partial_axis": True,
                "position": [0.025, 0.075, 0.925, 0.875]
            },
            "limits": {
                "range_temp_c": tem,
                "range_humidity_g_kg": hum,
                "altitude_m": altitude,
                "step_temp": .5
            },

            "saturation": {"color": [0, .3, 1.], "linewidth": 1, "linestyle": "-"},
            "constant_rh": {"color": [0.0, 0.498, 1.0, .7], "linewidth": 1, "linestyle": ":"},
            "constant_v": {"color": [0.0, 0.502, 0.337], "linewidth": 1, "linestyle": "--"},
            "constant_h": {"color": [0.251, 0.0, 0.502], "linewidth": 1, "linestyle": "--"},
            "constant_wet_temp": {"color": [0.498, 0.875, 1.0], "linewidth": 1, "linestyle": "-."},
            "constant_dry_temp": {"color": [0.855, 0.145, 0.114], "linewidth": 1, "linestyle": ":"},
            "constant_humidity": {"color": [0.0, 0.125, 0.376], "linewidth": 1, "linestyle": ":"},

            "chart_params": {
                "with_constant_rh": True,
                "constant_rh_label": "Constant relative humidity",
                "constant_rh_curves": [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "constant_rh_labels": [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "constant_rh_labels_loc": 0.95,

                "with_constant_v": False,
                "constant_v_label": "Constant specific volume",
                "constant_v_step": 0.02,
                "range_vol_m3_kg": [0.78, 1.22],
                "constant_v_labels": [0.86, 0.90, ],
                "constant_v_labels_loc": 1,

                "with_constant_h": False,
                "constant_h_label": "Constant enthalpy",
                "constant_h_step": 10,
                "range_h": [5, 155],
                "constant_h_labels": [5, 15, 25, 65],
                "constant_h_labels_loc": 1,

                "with_constant_wet_temp": True,
                "constant_wet_temp_label": "Constant wet bulb temperature",
                "constant_wet_temp_step": 5,
                "range_wet_temp": [-10, 45],
                "constant_wet_temp_labels": [0, 5, 10, 15, 20, 25, 30, 35],
                "constant_wet_temp_labels_loc": 0.05,

                "with_constant_dry_temp": True,
                "constant_temp_label": "Dry bulb temperature",
                "constant_temp_step": 5,
                "constant_temp_label_step": 5,
                "constant_temp_label_include_limits": True,

                "with_constant_humidity": True,
                "constant_humid_label": "Absolute humidity",
                "constant_humid_step": 4,
                "constant_humid_label_step": 4,
                "constant_humid_label_include_limits": True,

                "with_zones": False,
            }
        }
        chart_custom_2 = chart.PsychroChart(custom_style)
        chart_custom_2.plot(ax8)


        if comf == 1 or comf == 0:
            zones_comf_P = {
                "zones": [
                    {  # upper_line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[0], points[1]],
                        "points_y": [points[2], points[3]],
                        "label": ""
                    },
                    {  # lower _line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[4], points[5]],
                        "points_y": [points[6], points[7]],
                        "label": ""
                    },
                    {  # left _line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[8], points[9]],
                        "points_y": [points[10], points[11]],
                        "label": ""
                    },
                    {  # right _line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[12], points[13]],
                        "points_y": [points[14], points[15]],
                        "label": ""
                    }

                ]}

            points_comf = {
                'point_10_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                              'marker': '.', 'markersize': 3},
                    'xy': (points[16], points[17])},
                'point_11_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[18], points[19])}
            }

            connectors_comf = [
                {'start': 'point_10_name',
                 'end': 'point_11_name',
                 'style': {'color': [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                           "linewidth": 3, "linestyle": "-"}},
            ]


            # plot of comfort zone
            chart_custom_2.append_zones(zones_comf_P)
            chart_custom_2.plot(ax8)
            chart_custom_2.plot_points_dbt_rh(points_comf, connectors_comf)

        if thm == 1:
            points_t = {
                'point_6_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[20], points[21])},
                'point_7_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[22], points[23])},
                'point_8_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[24], points[25])},
                'point_9_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[26], points[27])}
            }

            connectors_t = [
                {'start': 'point_6_name',
                 'end': 'point_7_name',
                 'style'
                 : {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_7_name',
                 'end': 'point_9_name',
                 'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_8_name',
                 'end': 'point_9_name',
                 'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}}

            ]
            chart_custom_2.plot_points_dbt_rh(points_t, connectors_t)
        #evap points[28.5, 80, 50, 14.43, 18, 20, 50, .0001]
        #evap points[30, 80, 50, 17.47, 18, 20, 50, .0001]
        #evap points[31, 80, 50, 19.6, 18, 20, 50, .0001]
        if evap == 1:
            points_evap = {
                'point_1_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[28], points[29])},
                'point_3_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[30], points[31])},
                'point_4_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[32], points[33])},
                'point_5_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[34], points[35])}

            }

            connectors_evap = [
                {'start': 'point_1_name',
                 'end': 'point_3_name',
                 'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_4_name',
                 'end': 'point_5_name',
                 'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}}
            ]
            chart_custom_2.plot_points_dbt_rh(points_evap, connectors_evap)
        #[28.5, 80, 39.587, 43.129, 39.587, 8.433, 24.34, 20]
        #[30, 80, 39.862, 46.344, 39.862, 8.310, 24.34, 20]
        #[31, 80, 40.212, 48.165, 40.212, 8.156, 24.34, 20]
        if sun == 1:
            points_sun = {
                'point_12_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.', 'markersize': 3},
                    'xy': (points[36], points[37])},
                'point_13_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[38], points[39])},
                'point_14_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[40], points[41])},
                'point_15_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[42], points[43])}
            }

            connectors_sun = [
                {'start': 'point_12_name',
                 'end': 'point_13_name',
                 'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_13_name',
                 'end': 'point_14_name',
                 'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_14_name',
                 'end': 'point_15_name',
                 'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
            ]
            chart_custom_2.plot_points_dbt_rh(points_sun, connectors_sun)

        ################ EPW points all #############

        if c[0] != 0:
            points_comf_epw = {'points_series_name': (dbt_comf, rh_comf)}
            my_comf_style1 = {'s': 1, 'alpha': .8, 'color': 'lightblue'}
            chart_custom_2.plot_points_dbt_rh(points_comf_epw, scatter_style=my_comf_style1)
        if c[1] !=0 :
            points_can_comf_epw_0 = {'points_series_name': (dbt_can_comf[0], rh_can_comf[0])}
            my_comf_style2_0 = {'s': 1, 'alpha': .8, 'color': 'green'}
            chart_custom_2.plot_points_dbt_rh(points_can_comf_epw_0, scatter_style=my_comf_style2_0)
        if c[2] != 0:
            points_can_comf_epw_1 = {'points_series_name': (dbt_can_comf[1], rh_can_comf[1])}
            my_comf_style2_1 = {'s': 1, 'alpha': .8, 'color': 'yellow'}
            chart_custom_2.plot_points_dbt_rh(points_can_comf_epw_1, scatter_style=my_comf_style2_1)
        if c[3] != 0:
            points_can_comf_epw_2 = {'points_series_name': (dbt_can_comf[2], rh_can_comf[2])}
            my_comf_style2_2 = {'s': 1, 'alpha': .8, 'color': 'orange'}
            chart_custom_2.plot_points_dbt_rh(points_can_comf_epw_2, scatter_style=my_comf_style2_2)
        if epw == 1:
            if  c[4] != 0:
                points_out_comf_epw = {'points_series_name': (dbt_out_comf, rh_out_comf)}
                my_comf_style3 = {'s': 1, 'alpha': .8, 'color': 'red'}
                chart_custom_2.plot_points_dbt_rh(points_out_comf_epw, scatter_style=my_comf_style3)
        # Remove self.draw() at the end, as this is for GUI. The plot will be saved by the backend script.
        pass


# Command-line handler for backend use
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Path to input JSON file')
    args, unknown = parser.parse_known_args()

    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            params = json.load(f)
        dbt = params['dbt']
        rh = params['rh']
        elevation = params['elevation']
        text = params.get('text', "0 - 0.5 m/s")
        comf = params.get('comf', 1)
        epw = params.get('epw', 1)
        evap = params.get('evap', 1)
        thm = params.get('thm', 1)
        sun = params.get('sun', 1)
        evap_efficiency = params.get('evap_efficiency', 80)
    else:
        # fallback to old argument parsing if needed
        dbt = rh = []
        elevation = 0
        text = "0 - 0.5 m/s"
        comf = epw = evap = thm = sun = 1
        evap_efficiency = 80

    consultant = PassiveDesignConsultant(dbt=dbt, rh=rh, elevation=elevation)
    consultant.psychrometric_graph(
        text=text,
        comf=comf,
        epw=epw,
        evap=evap,
        thm=thm,
        sun=sun,
        custom_dbt=dbt,
        custom_rh=rh,
        evap_efficiency=evap_efficiency
    )
    import io
    buf = io.StringIO()
    plt.savefig(buf, format='svg')
    buf.seek(0)
    print(buf.read())
