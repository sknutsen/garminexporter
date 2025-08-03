import os
from garmin_fit_sdk import Decoder, Stream, Profile
from models import *

def parse_fit_files():
    rootpath: str = "activities/"

    f = []
    for (dirpath, dirnames, filenames) in os.walk(rootpath):
        f.extend(filenames)
        break
    
    current_fit_file: FITFile

    fields = set()

    fit_files = []

    for file in sorted(f):
        if file[-4:] == ".fit":
            fit_files.append(file)

    def mesg_listener(mesg_num, message: dict):
        if mesg_num == Profile['mesg_num']['ACTIVITY']:
            try:
                current_fit_file.activities.append(Activity(
                    event=message.get("event"),
                    event_type=message.get("event_type"),
                    local_timestamp=message.get("local_timestamp"),
                    num_sessions=message.get("num_sessions"),
                    timestamp=message.get("timestamp"),
                    total_timer_time=message.get("total_timer_time"),
                    type=message.get("type"),
                ))
            except Exception as e:
                print("ACTIVITY - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['DEVICE_INFO']:
            try:
                current_fit_file.device_info.append(DeviceInfo(
                    device_index=message.get("device_index"),
                    device_type=message.get("device_type"),
                    garmin_product=message.get("garmin_product"),
                    local_device_type=message.get("local_device_type"),
                    manufacturer=message.get("manufacturer"),
                    product=message.get("product"),
                    serial_number=message.get("serial_number"),
                    software_version=message.get("software_version"),
                    source_type=message.get("source_type"),
                    timestamp=message.get("timestamp"),
                ))
            except Exception as e:
                print("DEVICE_INFO - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['DEVICE_SETTINGS']:
            try:
                current_fit_file.device_settings.append(DeviceSettings(
                    active_time_zone=message.get("active_time_zone"),
                    activity_tracker_enabled=message.get("activity_tracker_enabled"),
                    auto_activity_detect=message.get("auto_activity_detect"),
                    autosync_min_steps=message.get("autosync_min_steps"),
                    autosync_min_time=message.get("autosync_min_time"),
                    backlight_mode=message.get("backlight_mode"),
                    date_mode=message.get("date_mode"),
                    lactate_threshold_autodetect_enabled=message.get("lactate_threshold_autodetect_enabled"),
                    mounting_side=message.get("mounting_side"),
                    move_alert_enabled=message.get("move_alert_enabled"),
                    time_mode=message.get("time_mode"),
                    time_offset=message.get("time_offset"),
                    time_zone_offset=message.get("time_zone_offset"),
                    utc_offset=message.get("utc_offset"),
                ))
            except Exception as e:
                print("DEVICE_SETTINGS - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['EVENT']:
            try:
                current_fit_file.events.append(Event(
                    data=message.get("data"),
                    event=message.get("event"),
                    event_group=message.get("event_group"),
                    event_type=message.get("event_type"),
                    hr_high_alert=message.get("hr_high_alert"),
                    hr_low_alert=message.get("hr_low_alert"),
                    speed_high_alert=message.get("speed_high_alert"),
                    speed_low_alert=message.get("speed_low_alert"),
                    timer_trigger=message.get("timer_trigger"),
                    timestamp=message.get("timestamp"),
                ))
            except Exception as e:
                print("EVENT - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['EXERCISE_TITLE']:
            try:
                current_fit_file.exercise_titles.append(ExerciseTitle(
                    exercise_category=message.get("exercise_category"),
                    exercise_name=message.get("exercise_name"),
                    message_index=message.get("message_index"),
                    wkt_step_name=message.get("wkt_step_name"),
                ))
            except Exception as e:
                print("EXERCISE_TITLE - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['FILE_CREATOR']:
            try:
                current_fit_file.file_creators.append(FileCreator(
                    software_version=message.get("software_version"),
                ))
            except Exception as e:
                print("FILE_CREATOR - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['FILE_ID']:
            try:
                current_fit_file.file_id = FileID(
                    garmin_product=message.get("garmin_product"),
                    manufacturer=message.get("manufacturer"),
                    product=message.get("product"),
                    serial_number=message.get("serial_number"),
                    time_created=message.get("time_created"),
                    type=message.get("type"),
                )
            except Exception as e:
                print("FILE_ID - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['GPS_METADATA']:
            try:
                current_fit_file.gps_metadata.append(GPSMetaData(
                    enhanced_altitude=message.get("enhanced_altitude"),
                    enhanced_speed=message.get("enhanced_speed"),
                ))
            except Exception as e:
                print("GPS_METADATA - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['HR']:
            try:
                raise Exception("HR not implemented")
            except Exception as e:
                print("HR - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['HRV']:
            try:
                raise Exception("HRV not implemented")
            except Exception as e:
                print("HRV - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['LAP']:
            try:
                current_fit_file.laps.append(Lap(
                    avg_cadence=message.get("avg_cadence"),
                    avg_flow=message.get("avg_flow"),
                    avg_fractional_cadence=message.get("avg_fractional_cadence"),
                    avg_heart_rate=message.get("avg_heart_rate"),
                    end_position_lat=message.get("end_position_lat"),
                    end_position_long=message.get("end_position_long"),
                    enhanced_avg_speed=message.get("enhanced_avg_speed"),
                    enhanced_max_speed=message.get("enhanced_max_speed"),
                    event=message.get("event"),
                    max_cadence=message.get("max_cadence"),
                    max_fractional_cadence=message.get("max_fractional_cadence"),
                    max_heart_rate=message.get("max_heart_rate"),
                    message_index=message.get("message_index"),
                    sport=message.get("sport"),
                    sport_profile_name=message.get("sport_profile_name"),
                    start_position_lat=message.get("start_position_lat"),
                    start_position_long=message.get("start_position_long"),
                    start_time=message.get("start_time"),
                    sub_sport=message.get("sub_sport"),
                    timestamp=message.get("timestamp"),
                    total_anaerobic_training_effect=message.get("total_anaerobic_training_effect"),
                    total_ascent=message.get("total_ascent"),
                    total_calories=message.get("total_calories"),
                    total_cycles=message.get("total_cycles"),
                    total_descent=message.get("total_descent"),
                    total_distance=message.get("total_distance"),
                    total_elapsed_time=message.get("total_elapsed_time"),
                    total_fractional_ascent=message.get("total_fractional_ascent"),
                    total_fractional_descent=message.get("total_fractional_descent"),
                    total_grit=message.get("total_grit"),
                    total_strides=message.get("total_strides"),
                    total_timer_time=message.get("total_timer_time"),
                    enhanced_max_altitude=message.get("enhanced_max_altitude"),
                    enhanced_min_altitude=message.get("enhanced_min_altitude"),
                    event_type=message.get("event_type"),
                    intensity=message.get("intensity"),
                    lap_trigger=message.get("lap_trigger"),
                ))
            except Exception as e:
                print("LAP - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['LENGTH']:
            try:
                raise Exception("LENGTH not implemented")
            except Exception as e:
                print("LENGTH - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['PAD']:
            try:
                raise Exception("PAD not implemented")
            except Exception as e:
                print("PAD - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['RECORD']:
            try:
                current_fit_file.records.append(Record(
                    accumulated_power=message.get("accumulated_power"),
                    activity_type=message.get("activity_type"),
                    cadence=message.get("cadence"),
                    cycle_length=message.get("cycle_length16"),
                    distance=message.get("distance"),
                    enhanced_altitude=message.get("enhanced_altitude"),
                    enhanced_speed=message.get("enhanced_speed"),
                    fractional_cadence=message.get("fractional_cadence"),
                    heart_rate=message.get("heart_rate"),
                    position_lat=message.get("position_lat"),
                    position_long=message.get("position_long"),
                    power=message.get("power"),
                    stance_time=message.get("stance_time"),
                    step_length=message.get("step_length"),
                    timestamp=message.get("timestamp"),
                    vertical_oscillation=message.get("vertical_oscillation"),
                    vertical_ratio=message.get("vertical_ratio"),
                ))
            except Exception as e:
                print("RECORD - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['SEGMENT_LAP']:
            try:
                raise Exception("SEGMENT_LAP not implemented")
            except Exception as e:
                print("SEGMENT_LAP - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['SET']:
            try:
                current_fit_file.sets.append(Set(
                    category=message.get("category"),
                    category_subtype=message.get("category_subtype"),
                    duration=message.get("duration"),
                    message_index=message.get("message_index"),
                    repetitions=message.get("repetitions"),
                    set_type=message.get("set_type"),
                    start_time=message.get("start_time"),
                    timestamp=message.get("timestamp"),
                    weight=message.get("weight"),
                    weight_display_unit=message.get("weight_display_unit"),
                    wkt_step_index=message.get("wkt_step_index"),
                ))
            except Exception as e:
                print("SET - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['SESSION']:
            try:
                current_fit_file.sessions.append(Session(
                    avg_cadence=message.get("avg_cadence"),
                    avg_flow=message.get("avg_flow"),
                    avg_fractional_cadence=message.get("avg_fractional_cadence"),
                    avg_heart_rate=message.get("avg_heart_rate"),
                    end_position_lat=message.get("end_position_lat"),
                    end_position_long=message.get("end_position_long"),
                    enhanced_avg_speed=message.get("enhanced_avg_speed"),
                    enhanced_max_speed=message.get("enhanced_max_speed"),
                    event=message.get("event"),
                    first_lap_index=message.get("first_lap_index"),
                    max_cadence=message.get("max_cadence"),
                    max_fractional_cadence=message.get("max_fractional_cadence"),
                    max_heart_rate=message.get("max_heart_rate"),
                    message_index=message.get("message_index"),
                    nec_lat=message.get("nec_lat"),
                    nec_long=message.get("nec_long"),
                    num_laps=message.get("num_laps"),
                    sport=message.get("sport"),
                    sport_profile_name=message.get("sport_profile_name"),
                    start_position_lat=message.get("start_position_lat"),
                    start_position_long=message.get("start_position_long"),
                    start_time=message.get("start_time"),
                    sub_sport=message.get("sub_sport"),
                    swc_lat=message.get("swc_lat"),
                    swc_long=message.get("swc_long"),
                    timestamp=message.get("timestamp"),
                    total_anaerobic_training_effect=message.get("total_anaerobic_training_effect"),
                    total_ascent=message.get("total_ascent"),
                    total_calories=message.get("total_calories"),
                    total_cycles=message.get("total_cycles"),
                    total_descent=message.get("total_descent"),
                    total_distance=message.get("total_distance"),
                    total_elapsed_time=message.get("total_elapsed_time"),
                    total_fractional_ascent=message.get("total_fractional_ascent"),
                    total_fractional_descent=message.get("total_fractional_descent"),
                    total_grit=message.get("total_grit"),
                    total_strides=message.get("total_strides"),
                    total_timer_time=message.get("total_timer_time"),
                    total_training_effect=message.get("total_training_effect"),
                    training_load_peak=message.get("training_load_peak"),
                    trigger=message.get("trigger"),
                ))
            except Exception as e:
                print("SESSION - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['SPORT']:
            try:
                current_fit_file.sports.append(Sport(
                    name=message.get("name"),
                    sport=message.get("sport"),
                    sub_sport=message.get("sub_sport"),
                ))
            except Exception as e:
                print("SPORT - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['SPLIT']:
            try:
                current_fit_file.splits.append(Split(
                    avg_speed=message.get("avg_speed"),
                    avg_vert_speed=message.get("avg_vert_speed"),
                    end_position_lat=message.get("end_position_lat"),
                    end_position_long=message.get("end_position_long"),
                    end_time=message.get("end_time"),
                    max_speed=message.get("max_speed"),
                    message_index=message.get("message_index"),
                    split_type=message.get("split_type"),
                    start_elevation=message.get("start_elevation"),
                    start_position_lat=message.get("start_position_lat"),
                    start_position_long=message.get("start_position_long"),
                    start_time=message.get("start_time"),
                    total_ascent=message.get("total_ascent"),
                    total_calories=message.get("total_calories"),
                    total_descent=message.get("total_descent"),
                    total_distance=message.get("total_distance"),
                    total_elapsed_time=message.get("total_elapsed_time"),
                    total_timer_time=message.get("total_timer_time"),
                ))
            except Exception as e:
                print("SPLIT - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['SPLIT_SUMMARY']:
            try:
                current_fit_file.split_summary.append(SplitSummary(
                    avg_heart_rate=message.get("avg_heart_rate"),
                    avg_speed=message.get("avg_speed"),
                    avg_vert_speed=message.get("avg_vert_speed"),
                    max_heart_rate=message.get("max_heart_rate"),
                    max_speed=message.get("max_speed"),
                    message_index=message.get("message_index"),
                    num_splits=message.get("num_splits"),
                    split_type=message.get("split_type"),
                    total_ascent=message.get("total_ascent"),
                    total_calories=message.get("total_calories"),
                    total_descent=message.get("total_descent"),
                    total_distance=message.get("total_distance"),
                    total_timer_time=message.get("total_timer_time"),
                ))
            except Exception as e:
                print("SPLIT_SUMMARY - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['TIME_IN_ZONE']:
            try:
                current_fit_file.time_in_zones.append(TimeInZone(
                    functional_threshold_power=message.get("functional_threshold_power"),
                    hr_calc_type=message.get("hr_calc_type"),
                    hr_zone_high_boundary=message.get("hr_zone_high_boundary"),
                    max_heart_rate=message.get("max_heart_rate"),
                    power_zone_high_boundary=message.get("power_zone_high_boundary"),
                    pwr_calc_type=message.get("pwr_calc_type"),
                    reference_index=message.get("reference_index"),
                    reference_mesg=message.get("reference_mesg"),
                    resting_heart_rate=message.get("resting_heart_rate"),
                    threshold_heart_rate=message.get("threshold_heart_rate"),
                    time_in_hr_zone=message.get("time_in_hr_zone"),
                    time_in_power_zone=message.get("time_in_power_zone"),
                    timestamp=message.get("timestamp"),
                ))
            except Exception as e:
                print("TIME_IN_ZONE - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['TRAINING_FILE']:
            try:
                current_fit_file.training_files.append(TrainingFile(
                    garmin_product=message.get("garmin_product"),
                    manufacturer=message.get("manufacturer"),
                    product=message.get("product"),
                    serial_number=message.get("serial_number"),
                    time_created=message.get("time_created"),
                    timestamp=message.get("timestamp"),
                    type=message.get("type"),
                ))
            except Exception as e:
                print("TRAINING_FILE - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                    
        elif mesg_num == Profile['mesg_num']['USER_PROFILE']:
            try:
                current_fit_file.user_profile.append(UserProfile(
                    activity_class=message.get("activity_class"),
                    depth_setting=message.get("depth_setting"),
                    dist_setting=message.get("dist_setting"),
                    elev_setting=message.get("elev_setting"),
                    gender=message.get("gender"),
                    height=message.get("height"),
                    height_setting=message.get("height_setting"),
                    hr_setting=message.get("hr_setting"),
                    language=message.get("language"),
                    position_setting=message.get("position_setting"),
                    resting_heart_rate=message.get("resting_heart_rate"),
                    sleep_time=message.get("sleep_time"),
                    speed_setting=message.get("speed_setting"),
                    temperature_setting=message.get("temperature_setting"),
                    wake_time=message.get("wake_time"),
                    weight=message.get("weight"),
                    weight_setting=message.get("weight_setting"),
                ))
            except Exception as e:
                print("USER_PROFILE - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
                
        elif mesg_num == Profile['mesg_num']['WORKOUT']:
            try:
                current_fit_file.workouts.append(Workout(
                    name=message.get("wkt_name"),
                    sport=message.get("sport"),
                    sub_sport=message.get("sub_sport"),
                    num_valid_steps=message.get("num_valid_steps"),
                    notes=message.get(17),
                    capabilities=message.get("capabilities"),
                ))
            except Exception as e:
                print("WORKOUT - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['WORKOUT_STEP']:
            try:
                current_fit_file.workout_steps.append(WorkoutStep(
                    index=message.get("message_index"),
                    custom_target_value_high=message.get("custom_target_value_high"),
                    custom_target_value_low=message.get("custom_target_value_low"),
                    duration_reps=message.get("duration_reps"),
                    duration_step=message.get("duration_step"),
                    duration_time=message.get("duration_time"),
                    duration_type=message.get("duration_type"),
                    duration_value=message.get("duration_value"),
                    equipment=message.get("equipment"),
                    exercise_category=message.get("exercise_category"),
                    exercise_name=message.get("exercise_name"),
                    exercise_weight=message.get("exercise_weight"),
                    intensity=message.get("intensity"),
                    name=message.get("name"),
                    notes=message.get("notes"),
                    repeat_steps=message.get("repeat_steps"),
                    target_type=message.get("target_type"),
                    target_value=message.get("target_value"),
                    weight_display_unit=message.get("weight_display_unit"),
                ))
            except Exception as e:
                print("WORKOUT_STEP - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == Profile['mesg_num']['ZONES_TARGET']:
            try:
                current_fit_file.zones_targets.append(ZonesTarget(
                    functional_threshold_power=message.get("functional_threshold_power"),
                    hr_calc_type=message.get("hr_calc_type"),
                    max_heart_rate=message.get("max_heart_rate"),
                    pwr_calc_type=message.get("pwr_calc_type"),
                    threshold_heart_rate=message.get("threshold_heart_rate"),
                ))
            except Exception as e:
                print("ZONES_TARGET - something failed: ", e)
                print(message)
                # for field in message:
                #     fields.add(field)
        
        elif mesg_num == 13:
            pass
        elif mesg_num == 22:
            pass
        elif mesg_num == 79:
            pass
        elif mesg_num == 104:
            pass
        elif mesg_num == 113:
            pass
        elif mesg_num == 125:
            pass
        elif mesg_num == 140:
            pass
        elif mesg_num == 141:
            pass
        elif mesg_num == 233:
            pass
        elif mesg_num == 288:
            pass
        elif mesg_num == 325:
            pass
        elif mesg_num == 326:
            pass
        elif mesg_num == 327:
            pass
        elif mesg_num == 394:
            pass
        elif mesg_num == 428:
            pass
        
        else:
            mesg_type = "MESSAGE TYPE NOT FOUND - " + str(mesg_num)
            for k, v in Profile['mesg_num'].items():
                if v == mesg_num:
                    mesg_type = k
            print("NOT SUPPORTED: ", mesg_type)
            # print(message)

    decoded_fit_files = []

    for file in fit_files:
        current_fit_file: FITFile = FITFile(
            file_id=0,
            activities=[],
            sessions=[],
            laps=[],
            records=[],
            device_info=[],
            events=[],
            user_profile=[],
            zones_targets=[],
            gps_metadata=[],
            sports=[],
            device_settings=[],
            time_in_zones=[],
            file_creators=[],
            exercise_titles=[],
            training_files=[],
            split_summary=[],
            splits=[],
            sets=[],
            workouts=[],
            workout_steps=[],
        )

        stream = Stream.from_file(rootpath + file)
        decoder = Decoder(stream)
        messages, errors = decoder.read(mesg_listener = mesg_listener)
        decoded_fit_files.append(current_fit_file)
        
        if len(errors) > 0:
            print(errors)
            break
        
    print(fields)
    return decoded_fit_files
