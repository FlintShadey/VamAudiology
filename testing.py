@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Registration logic goes here...
        return jsonify(success=True)
    else:
        # Return validation errors
        return jsonify(success=False, errors=form.errors), 400
