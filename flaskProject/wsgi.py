from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@app.cli.command('create-user')
def create_user():
    from blog.models import User

    db.session.add(
        User(first_name='Дмитрий',
             last_name='Посвянский',
             email='posv@mail.ru',
             password=generate_password_hash('1234'))
    )
    db.session.commit()

    print('done! create user.')


@app.cli.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    for name in [
        'flask',
        'django',
        'python',
        'sqlite',
        'coding'
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print('Done!')
