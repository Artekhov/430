import json

# Чтение данных из файлов
with open(sys.argv[1], 'r') as tests_file:
	tests_data = json.load(tests_file)

with open(sys.argv[2], 'r') as values_file:
	values_data = json.load(values_file)

# Функция для заполнения значений тестов
def fill_test_values(test, values):
	if 'id' in test and test['id'] in values:
		test['value'] = values[test['id']]
		if 'values' in test:
			for subtest in test['values']:
				fill_test_values(subtest, values)

# Заполнение значений тестов
fill_test_values(tests_data, values_data)

# Запись данных в файл report.json
with open('report.json', 'w') as report_file:
	json.dump(tests_data, report_file, indent=4)
