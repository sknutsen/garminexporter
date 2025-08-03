from datetime import datetime
from dataclasses import dataclass, field, fields, _MISSING_TYPE

@dataclass
class FITData:
    def __post_init__(self):
        # Loop through the fields
        for field in fields(self):
            # If there is a default and the value of the field is none we can assign a value
            if not isinstance(field.default, _MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)
    
@dataclass
class FileID(FITData):
    serial_number: int
    time_created: datetime
    manufacturer: str
    product: int
    type: str
    garmin_product: str
    
@dataclass
class Activity(FITData):
    timestamp: datetime
    total_timer_time: float
    local_timestamp: int
    num_sessions: int
    type: str
    event: str
    event_type: str
    
@dataclass
class Session(FITData):
    timestamp: datetime
    start_time: datetime
    start_position_lat: int
    start_position_long: int
    total_elapsed_time: float
    total_timer_time: float
    total_distance: float
    total_cycles: int
    nec_lat: int
    nec_long: int
    swc_lat: int
    swc_long: int
    end_position_lat: int
    end_position_long: int
    sport_profile_name: str
    enhanced_avg_speed: float
    enhanced_max_speed: float
    training_load_peak: float
    total_grit: int
    avg_flow: int
    message_index: int
    total_calories: int
    total_ascent: int
    total_descent: int
    first_lap_index: int
    num_laps: int
    event: str
    sport: str
    sub_sport: str
    avg_heart_rate: int
    max_heart_rate: int
    avg_cadence: int
    max_cadence: int
    total_training_effect: float
    trigger: str
    avg_fractional_cadence: float
    max_fractional_cadence: float
    total_anaerobic_training_effect: float
    total_fractional_ascent: float
    total_fractional_descent: float
    total_strides: int
    
@dataclass
class Lap(FITData):
    timestamp: datetime
    start_time: datetime
    start_position_lat: int
    start_position_long: int
    total_elapsed_time: float
    total_timer_time: float
    total_distance: float
    total_cycles: int
    end_position_lat: int
    end_position_long: int
    sport_profile_name: str
    enhanced_avg_speed: float
    enhanced_max_speed: float
    enhanced_max_altitude: float
    enhanced_min_altitude: float
    total_grit: int
    avg_flow: int
    message_index: int
    total_calories: int
    total_ascent: int
    total_descent: int
    event: str
    event_type: str
    avg_heart_rate: int
    max_heart_rate: int
    avg_cadence: int
    max_cadence: int
    intensity: str
    lap_trigger: str
    sport: str
    sub_sport: str
    avg_fractional_cadence: float
    max_fractional_cadence: float
    total_anaerobic_training_effect: float
    total_fractional_ascent: float
    total_fractional_descent: float
    total_strides: int
    
@dataclass
class Record(FITData):
    step_length: int
    enhanced_speed: float
    power: float
    enhanced_altitude: float
    distance: float
    position_lat: float
    position_long: float
    accumulated_power: float
    cadence: int
    timestamp: datetime
    fractional_cadence: float
    vertical_ratio: float
    cycle_length: float
    activity_type: str
    vertical_oscillation: float
    stance_time: float
    heart_rate: int
    
@dataclass
class DeviceInfo(FITData):
    source_type: str
    serial_number: int
    software_version: float
    device_index: int
    timestamp: datetime
    garmin_product: str
    manufacturer: str
    device_type: int
    local_device_type: str
    product: int
    
@dataclass
class Event(FITData):
    data: int
    event_type: str
    hr_low_alert: int
    hr_high_alert: int
    timestamp: datetime
    timer_trigger: str
    event_group: int
    event: str
    speed_low_alert: float
    speed_high_alert: float
    
@dataclass
class UserProfile(FITData):
    position_setting: str
    activity_class: int
    speed_setting: str
    weight: float
    dist_setting: str
    gender: str
    hr_setting: str
    weight_setting: str
    sleep_time: int
    wake_time: int
    temperature_setting: str
    resting_heart_rate: int
    height_setting: str
    height: float
    language: str
    elev_setting: str
    depth_setting: str
    
@dataclass
class ZonesTarget(FITData):
    hr_calc_type: str
    threshold_heart_rate: int
    max_heart_rate: int
    functional_threshold_power: int
    pwr_calc_type: str
    
@dataclass
class GPSMetaData(FITData):
    enhanced_altitude: float
    enhanced_speed: float
    
@dataclass
class Sport(FITData):
    name: list
    sport: str
    sub_sport: str
    
@dataclass
class DeviceSettings(FITData):
    time_zone_offset: int
    auto_activity_detect: int
    autosync_min_time: int
    activity_tracker_enabled: int
    mounting_side: str
    time_mode: str
    autosync_min_steps: int
    lactate_threshold_autodetect_enabled: int
    utc_offset: int
    active_time_zone: int
    time_offset: int
    backlight_mode: str
    date_mode: str
    move_alert_enabled: int
    
@dataclass
class TimeInZone(FITData):
    max_heart_rate: int
    hr_calc_type: str
    time_in_power_zone: list
    threshold_heart_rate: int
    timestamp: datetime
    reference_mesg: str
    time_in_hr_zone: list
    hr_zone_high_boundary: list
    resting_heart_rate: int
    reference_index: int
    functional_threshold_power: int
    power_zone_high_boundary: list
    pwr_calc_type: str
    
@dataclass
class FileCreator(FITData):
    software_version: int
    
@dataclass
class ExerciseTitle(FITData):
    wkt_step_name: list
    exercise_name: int
    exercise_category: int
    message_index: int
    
@dataclass
class TrainingFile(FITData):
    type: str
    product: int
    garmin_product: str
    timestamp: datetime
    time_created: datetime
    serial_number: int
    manufacturer: str

@dataclass
class SplitSummary(FITData):
    total_calories: int
    avg_heart_rate: int
    max_heart_rate: int
    total_ascent: int
    total_descent: int
    split_type: str
    avg_vert_speed: float
    num_splits: int
    total_distance: float
    total_timer_time: float
    max_speed: float
    avg_speed: float
    message_index: int
    
@dataclass
class Split(FITData):
    total_distance: float
    total_ascent: int
    total_descent: int
    message_index: int
    split_type: str
    avg_vert_speed: float
    total_elapsed_time: float
    total_calories: int
    end_time: datetime
    max_speed: float
    avg_speed: float
    end_position_lat: float
    end_position_long: float
    start_elevation: int
    start_time: datetime
    start_position_lat: float
    start_position_long: float
    total_timer_time: float

@dataclass
class Set(FITData):
    weight_display_unit: str
    start_time: datetime
    message_index: int
    weight: float
    category: list
    duration: float
    timestamp: datetime
    wkt_step_index: int
    category_subtype: list
    set_type: str
    repetitions: int

@dataclass
class WorkoutStep(FITData):
    index: int
    exercise_category: str
    exercise_name: int
    exercise_weight: int
    weight_display_unit: str
    name: str
    duration_type: str
    duration_value: int
    duration_reps: int
    duration_time: int
    duration_step: int
    target_type: str
    target_value: int
    custom_target_value_low: int
    custom_target_value_high: int
    intensity: str
    notes: str
    equipment: str
    repeat_steps: int

@dataclass
class Workout(FITData):
    name: str
    sport: str
    sub_sport: str
    num_valid_steps: int
    notes: str
    capabilities: int

@dataclass
class FITFile(FITData):
    file_id: FileID
    activities: list
    sessions: list
    laps: list
    records: list
    device_info: list
    events: list
    user_profile: list
    zones_targets: list
    gps_metadata: list
    sports: list
    device_settings: list
    time_in_zones: list
    file_creators: list
    exercise_titles: list
    training_files: list
    split_summary: list
    splits: list
    sets: list
    workouts: list
    workout_steps: list
