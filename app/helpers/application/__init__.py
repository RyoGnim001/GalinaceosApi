def register_blueprints(app):
    from app.controllers.galinaceos_controller import bp as galinaceos_bp

    app.register_blueprint(galinaceos_bp)