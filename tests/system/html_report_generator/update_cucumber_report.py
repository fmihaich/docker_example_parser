import argparse

import base64
import json
import os


DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'output'))


class ReportElementKey:
    elements = 'elements'
    elem_type = 'type'
    elem_steps = 'steps'
    name = 'name'
    step_result = 'result'
    step_status = 'status'
    step_embeddings = 'embeddings'


class ReportElementType:
    scenario = 'scenario'


class StepKey:
    result = 'result'
    status = 'status'
    embeddings = 'embeddings'


class StepStatus:
    failed = 'failed'
    skipped = 'skipped'


def read_cucumber_json(input_file):
    with open(input_file, 'r') as f:
        cucumber_data = f.read()

    return json.loads(cucumber_data)


def write_cucumber_file(output_file, report):
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=4)
    

def is_scenario_with_failing_step(scenario_steps):
    return any([step for step in scenario_steps if step[StepKey.result][StepKey.status] == StepStatus.failed])


def get_related_step_file(scenario_files, step_name):
    step_file_name_ended = step_name.replace(' ', '_') + '.png'
    return next((f for f in scenario_files if f.endswith(step_file_name_ended)), None)


def get_image_bytes(img_file_path):
    return base64.b64encode(open(img_file_path, "rb").read())


def update_report(report, result_dir_source, just_failing_img):
    for feature in report:
        for element in feature[ReportElementKey.elements]:
            if element[ReportElementKey.elem_type] == ReportElementType.scenario:
                scenario_with_failing_step = is_scenario_with_failing_step(
                    scenario_steps=element[ReportElementKey.elem_steps])
                if (not just_failing_img) or scenario_with_failing_step:
                    scenario_dir = os.path.join(result_dir_source, element[ReportElementKey.name].replace(' ', '_'))
                    scenario_files = os.listdir(scenario_dir) if os.path.exists(scenario_dir) else []
                    # Add all steps images
                    for step in element[ReportElementKey.elem_steps]:
                        step_file = get_related_step_file(scenario_files, step_name=step[ReportElementKey.name])
                        step_file_path = os.path.join(scenario_dir, step_file) if step_file else ''
                        if os.path.exists(step_file_path):
                            img_bytes = get_image_bytes(step_file_path)
                            step[StepKey.embeddings] = [
                                {
                                    "mime_type": "image/png",
                                    "data": img_bytes.decode("utf-8")
                                }
                            ]
    return report


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str, help='The cucumber json input file path')
    parser.add_argument(
        '-o', '--output', required=True, type=str,
        help='The cucumber json out file. It could be the same than the input one.')
    parser.add_argument('-b', '--browser', required=True, type=str, help='The browser to use as folder path')
    parser.add_argument(
        '-d', '--output-dir', required=False, type=str, help='The output directory where test result and images are',
        default=DEFAULT_OUTPUT_DIR)
    parser.add_argument('--just-failing-img', dest='just_failing_img', action='store_true', default=False)

    return parser.parse_args()


if __name__ == '__main__':
    print('Updating cucumber report to include images in failed and automatically skipped scenarios')

    args = get_args()

    cucumber_input_file_path = os.path.abspath(args.input)
    cucumber_output_file_path = os.path.abspath(args.output)

    print('Reading cucumber json file: {0}'.format(cucumber_input_file_path))
    execution_summary = read_cucumber_json(input_file=cucumber_input_file_path)

    result_dir = os.path.join(args.output_dir, args.browser)
    print('Updating cucumber json using images stored in: {0}'.format(result_dir))
    updated_report = \
        update_report(execution_summary, result_dir_source=result_dir, just_failing_img=args.just_failing_img)

    print('Writing cucumber json file with added images to: {0}'.format(cucumber_output_file_path))
    write_cucumber_file(output_file=cucumber_output_file_path, report=updated_report)

