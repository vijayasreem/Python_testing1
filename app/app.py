from flask import Flask, request, jsonify

app = Flask(__name__) 

@app.route('/BajajAllianzGroupSampoornaJeevanSurakshaPolicyValidation', methods=['POST'])
def validate_policy():
    # Get the json data
    data = request.get_json()

    # Retrieve the values from the json data
    min_sum_assured = data['minSumAssured']
    max_sum_assured = data['maxSumAssured']
    min_age_limit = data['minAgeLimit']
    max_age_limit = data['maxAgeLimit']
    annual_income = data['annualIncome']
    sum_assured_ranges = data['sumAssuredRanges']
    policy_tenure_ranges = data['policyTenureRanges']
    otp_authentication = data['OTPAuthentication']

    # Validation checks
    if min_sum_assured is None or max_sum_assured is None:
        return jsonify({"error": "Minimum and maximum sum assured not defined"})

    if min_age_limit is None or max_age_limit is None:
        return jsonify({"error": "Minimum and maximum age limits not defined"})

    if annual_income < 40000:
        return jsonify({"error": "Member is not eligible for insurance coverage"})

    if sum_assured_ranges not in [50000, 100000, 150000, 200000]:
        return jsonify({"error": "Sum assured ranges are not correct"})

    if policy_tenure_ranges not in [12, 15, 18, 24]:
        return jsonify({"error": "Policy tenure ranges are not correct"})

    if otp_authentication is False:
        return jsonify({"error": "OTP authentication not received"})

    # If all the checks pass, return a success message
    return jsonify({"message": "Policy validation successful"})

if __name__ == '__main__':
    app.run(debug=True)