# Created by Elena Roncolino

import csv
import json
from collections import defaultdict

w = open("metrics.txt", "w")


# Main method that open the csv file to be read and calls the methods to analyse the file
def main():
    columns = defaultdict(list)

    with open('results.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            for (i, v) in enumerate(row):
                columns[i].append(v)

    w.write("********************* METRICS *********************\n\n")

    number_of_screens(columns)
    components_count(columns)
    computational_concepts_blocks(columns)


# Counts the number of screens
def number_of_screens(columns):
    screen_list = []

    for item in columns[1]:
        if item not in screen_list:
            screen_list.append(item)

    w.write("Names of screens: ")
    w.write(json.dumps(screen_list))
    w.write("\nNumber of screens: %d" % len(screen_list))
    w.write("")


# Counts the number of components
def components_count(columns):
    user_interface_dictionary = {
        "Button": 0,
        "CheckBox": 0,
        "DatePicker": 0,
        "Image": 0,
        "Label": 0,
        "ListPicker": 0,
        "ListView": 0,
        "Notifier": 0,
        "PasswordTextBox": 0,
        "Slider": 0,
        "Spinner": 0,
        "Switch": 0,
        "TextBox": 0,
        "TimePicker": 0,
        "WebViewer": 0
    }

    layout_dictionary = {
        "HorizontalArrangement": 0,
        "HorizontalScrollArrangement": 0,
        "TableArrangement": 0,
        "VerticalArrangement": 0,
        "VerticalScrollArrangement": 0
    }

    media_dictionary = {
        "Camcorder": 0,
        "Camera": 0,
        "ImagePicker": 0,
        "Sound": 0,
        "SoundRecorder": 0,
        "SpeechRecognizer": 0,
        "TextToSpeech": 0,
        "VideoPlayer": 0,
        "YandexTranslate": 0
    }

    drawing_animation_dictionary = {
        "Ball": 0,
        "Canvas": 0,
        "ImageSprite": 0
    }

    maps_dictionary = {
        "Circle": 0,
        "FeatureCollection": 0,
        "LineString": 0,
        "Map": 0,
        "Marker": 0,
        "Polygon": 0,
        "Rectangle": 0
    }

    sensors_dictionary = {
        "AccelerometerSensor": 0,
        "BarcodeScanner": 0,
        "Clock": 0,
        "GyroscopeSensor": 0,
        "LocationSensor": 0,
        "NearField": 0,
        "OrientationSensor": 0,
        "Pedometer": 0,
        "ProximitySensor": 0
    }

    social_dictionary = {
        "ContactPicker": 0,
        "EmailPicker": 0,
        "PhoneCall": 0,
        "PhoneNumberPicker": 0,
        "Sharing": 0,
        "Texting": 0,
        "Twitter": 0
    }

    storage_dictionary = {
        "File": 0,
        "FusiontablesControl": 0,
        "TinyDB": 0,
        "TinyWebDB": 0
    }

    connectivity_dictionary = {
        "ActivityStarter": 0,
        "BluetoothClient": 0,
        "BluetoothServer": 0,
        "Web": 0
    }

    lego_mindstorms_dictionary = {
        "NxtDrive": 0,
        "NxtColorSensor": 0,
        "NxtLightSensor": 0,
        "NxtSoundSensor": 0,
        "NxtTouchSensor": 0,
        "NxtUltrasonicSensor": 0,
        "NxtDirectCommands": 0,
        "Ev3Motors": 0,
        "Ev3ColorSensor": 0,
        "Ev3GyroSensor": 0,
        "Ev3TouchSensor": 0,
        "Ev3UltrasonicSensor": 0,
        "Ev3Sound": 0,
        "Ev3UI": 0,
        "Ev3Commands": 0
    }

    experimental_dictionary = {
        "CloudDB": 0,
        "FirebaseDB": 0
    }

    for item in columns[5]:
        if item in user_interface_dictionary:
            user_interface_dictionary[item] += 1
        elif item in layout_dictionary:
            layout_dictionary[item] += 1
        elif item in media_dictionary:
            media_dictionary[item] += 1
        elif item in drawing_animation_dictionary:
            drawing_animation_dictionary[item] += 1
        elif item in maps_dictionary:
            maps_dictionary[item] += 1
        elif item in sensors_dictionary:
            sensors_dictionary[item] += 1
        elif item in social_dictionary:
            social_dictionary[item] += 1
        elif item in storage_dictionary:
            storage_dictionary[item] += 1
        elif item in connectivity_dictionary:
            connectivity_dictionary[item] += 1
        elif item in lego_mindstorms_dictionary:
            lego_mindstorms_dictionary[item] += 1
        elif item in experimental_dictionary:
            experimental_dictionary[item] += 1

    w.write("\nUser interface components: ")
    w.write(json.dumps(user_interface_dictionary))
    w.write("\nNumber of user interface components: %d" % len(user_interface_dictionary))
    w.write("\n")

    w.write("\nLayout components: ")
    w.write(json.dumps(layout_dictionary))
    w.write("\nNumber of layout components: %d" % len(layout_dictionary))
    w.write("\n")

    w.write("\nMedia components: ")
    w.write(json.dumps(media_dictionary))
    w.write("\nNumber of media components %d" % len(media_dictionary))
    w.write("\n")

    w.write("\nDrawing animation components: ")
    w.write(json.dumps(drawing_animation_dictionary))
    w.write("\nNumber of drawing animation components: %d" % len(drawing_animation_dictionary))
    w.write("\n")

    w.write("\nMaps components: ")
    w.write(json.dumps(maps_dictionary))
    w.write("\nNumber of maps components: %d" % len(maps_dictionary))
    w.write("\n")

    w.write("\nSensors components: ")
    w.write(json.dumps(sensors_dictionary))
    w.write("\nNumber of sensors components: %d" % len(sensors_dictionary))
    w.write("\n")

    w.write("\nSocial components: ")
    w.write(json.dumps(social_dictionary))
    w.write("\nNumber of social components: %d" % len(social_dictionary))
    w.write("\n")

    w.write("\nStorage components: ")
    w.write(json.dumps(storage_dictionary))
    w.write("\nNumber of storage components: %d" % len(storage_dictionary))
    w.write("\n")

    w.write("\nConnectivity components: ")
    w.write(json.dumps(connectivity_dictionary))
    w.write("\nNumber of connectivity components: %d" % len(connectivity_dictionary))
    w.write("")

    w.write("Lego mindstorms components: ")
    w.write(json.dumps(lego_mindstorms_dictionary))
    w.write("Number of lego mindstorms components: %d" % len(lego_mindstorms_dictionary))
    w.write("\n")

    w.write("\nExperimental components: ")
    w.write(json.dumps(experimental_dictionary))
    w.write("\nNumber of experimental components: %d" % len(experimental_dictionary))
    w.write("\n")

    tnc = len(user_interface_dictionary) + len(layout_dictionary) + len(media_dictionary) + \
        len(drawing_animation_dictionary) + len(maps_dictionary) + len(sensors_dictionary) + len(social_dictionary) + \
        len(storage_dictionary) + len(connectivity_dictionary) + len(lego_mindstorms_dictionary) + \
        len(experimental_dictionary)

    w.write("\nTotal number of components (TNC): %d" % tnc)

    noub = 0

    for x, y in user_interface_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in layout_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in media_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in drawing_animation_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in maps_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in sensors_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in social_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in storage_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in connectivity_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in lego_mindstorms_dictionary.items():
        if y != 0:
            noub += 1

    for x, y in experimental_dictionary.items():
        if y != 0:
            noub += 1

    w.write("\nTotal number of unique blocks (NOUB): %d" % noub)
    w.write("\n")


def computational_concepts_blocks(columns):
    variable_cc_blocks = {
        "component_set_get": 0,
        "global_declaration": 0
    }

    procedure_cc_blocks = {
        "component_method": 0
    }

    logic_cc_blocks = {
        "logic_boolean": 0,  # true false not
        "logic_compare": 0,  # = !=
        "logic_operation": 0  # and or
    }

    loop_cc_blocks = {
        # todo
    }

    conditional_cc_blocks = {
        # todo
    }

    list_cc_blocks = {
        # todo
    }

    for item in columns[5]:
        if item in variable_cc_blocks:
            variable_cc_blocks[item] += 1
        elif item in procedure_cc_blocks:
            procedure_cc_blocks[item] += 1
        elif item in logic_cc_blocks:
            logic_cc_blocks[item] += 1
        elif item in loop_cc_blocks:
            loop_cc_blocks[item] += 1
        elif item in conditional_cc_blocks:
            conditional_cc_blocks[item] += 1
        elif item in list_cc_blocks:
            list_cc_blocks[item] += 1

    w.write("\nComputational Concepts (CC) blocks analysis: ")
    w.write("\nVariable CC blocks: %d" % len(variable_cc_blocks))
    w.write("\nProcedure CC blocks: %d" % len(procedure_cc_blocks))
    w.write("\nLogic CC blocks: %d" % len(logic_cc_blocks))
    w.write("\nLoop CC blocks: %d" % len(loop_cc_blocks))
    w.write("\nConditional CC blocks: %d" % len(conditional_cc_blocks))
    w.write("\nList CC blocks: %d" % len(list_cc_blocks))


if __name__ == "__main__":
    main()
