def generate_recommendations(password,analysis_result,warning,entropy):
    recommendations = []

    if analysis_result['length'] < 8:
        recommendations.append("Consider using a longer password (at least 8 characters).")

    if analysis_result['length'] < 12:
        recommendations.append("Consider using a longer password for a better security"
        "(at least 12 characters).")

    if not analysis_result['has_uppercase']:
        recommendations.append("Include at least one uppercase letter.")

    if not analysis_result['has_lowercase']:
        recommendations.append("Include at least one lowercase letter.")

    if not analysis_result['has_digit']:
        recommendations.append("Include at least one digit.")

    if not analysis_result['has_special']:
        recommendations.append("Include at least one special character (e.g., !, @, #, $).")

    if entropy < 50:
        recommendations.append("Increase the complexity of your password to improve entropy.")

    if warning:
        recommendations.append("Avoid common patterns and repeated characters in your password.")

    if not recommendations:
        recommendations.append("Your password is strong and follows best practices.")

    return recommendations