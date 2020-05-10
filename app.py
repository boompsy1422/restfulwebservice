import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('Courses.JSON') as json_data:
    d = json.load(json_data)
    list_of_courses = []
    for data in d['courses']:
    	list_of_courses.append(data)

with open('Student.JSON') as student_data:
	a = json.load(student_data)
	list_of_students = []
	for student in a['students']:
		list_of_students.append(student)
	print("list_of_students: ", list_of_students)

@app.route('/', methods =['GET'])
def home():
	return render_template("index.html")

@app.route('/courses', methods =['GET'])
def all_courses():
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(d)
	return render_template("index.html",list_data=list_of_courses)

@app.route('/courses/<string:course_id>', methods =['GET'])
def course_by_id(course_id):
	cou = [courses for courses in list_of_courses if courses['courseid'] == course_id]
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(cou)
	return render_template("index.html",list_data=cou)

@app.route('/courses/<string:course_id>/student', methods =['GET'])
def student_by_course_id(course_id):
	course_student = [students for students in list_of_students if students['courseid'] == course_id]
	# print("course_student: ", str(course_student))
	student = course_student[0]['student']
	# print("course_student: ", str(student))
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(course_student)
	return render_template("index.html", list_student_data=student, course_id=course_id)

@app.route('/courses/<string:course_id>/student/<string:student_id>', methods =['GET'])
def student_by_course_id_student_id(course_id, student_id):
	course_student = [students for students in list_of_students if students['courseid'] == course_id]
	# print("empire_army: ", str(empire_army))
	# print("empire_army[0]: ", str(empire_army[0]))
	# print("army: ", str(empire_army[0]['army']))
	stu = [student for student in course_student[0]['student'] if student['studentid'] == student_id]
	print("single student: ", stu)
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(stu)
	return render_template("index.html", list_army_data=stu, course_id=course_id)

if __name__ == '__main__':
	 app.run(host='127.0.0.1', port=4221)
