from flask import Blueprint, request, render_template, redirect, url_for, flash
from db import mysql

contacts = Blueprint('contacts', __name__, template_folder='app/templates')


@contacts.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts=data)


@contacts.route('/add_project', methods=['POST'])
def add_project():
    if request.method == 'POST':
        autor = request.form['autor']
        titulo = request.form['titulo']
        objetivo = request.form['objetivo']
        abstract = request.form['abstract']
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO usuario (autor, titulo, objetivo, abstract) VALUES (%s,%s,%s,%s)", (autor, titulo, objetivo, abstract))
            mysql.connection.commit()
            flash('Project Added successfully')
            return redirect(url_for('contacts.Index'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('contacts.Index'))


@contacts.route('/edit/<id>', methods=['POST', 'GET'])
def get_project(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-project.html', contact=data[0])


@contacts.route('/update/<id>', methods=['POST'])
def update_project(id):
    if request.method == 'POST':
        autor = request.form['autor']
        titulo = request.form['titulo']
        objetivo = request.form['objetivo']
        abstract = request.form['abstract']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE usuario
            SET autor = %s,
                titulo = %s,
                objetivo = %s,
                abstract = %s 
            WHERE id = %s
        """, (autor, titulo, objetivo, abstract, id))
        flash('Project Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('contacts.Index'))


@contacts.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_project(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuario WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Project Removed Successfully')
    return redirect(url_for('contacts.Index'))
