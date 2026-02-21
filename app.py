import os
from flask import Flask, session, request, redirect, url_for, render_template
import data
import psychometric_engine

app = Flask(__name__)
# Use a strong secret key for session management
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(32))

@app.route('/')
def home():
    """
    Landing page. Resets session state.
    """
    session.clear()
    session['q_idx'] = 0
    session['u_v'] = []
    session.modified = True
    
    return render_template('index.html', step='HOME')

@app.route('/test', methods=['GET', 'POST'])
def test():
    """
    Handles the simulation progression and scenario scoring.
    """
    # Safety check: ensure session variables exist
    if 'q_idx' not in session or 'u_v' not in session:
        return redirect(url_for('home'))

    scenarios = data.get_assessment_data()
    q_idx = session['q_idx']

    if request.method == 'POST':
        selected_option_idx = request.form.get('selected_option')
        
        # Validate form submission
        if selected_option_idx is not None and selected_option_idx.isdigit():
            selected_option_idx = int(selected_option_idx)
            
            # Retrieve the score vector for the selected option
            try:
                current_scenario = scenarios[q_idx]
                score_vector = current_scenario['opts'][selected_option_idx]['s']
                
                # Append formatted dictionary as required by psychometric_engine
                session['u_v'].append({'s': score_vector})
                session['q_idx'] += 1
                session.modified = True
            except (IndexError, KeyError):
                # Handle potential manipulation of form data
                return redirect(url_for('test'))

        return redirect(url_for('test'))

    # GET request processing
    if q_idx >= len(scenarios):
        return redirect(url_for('results'))

    current_scenario = scenarios[q_idx]
    return render_template(
        'index.html', 
        step='TEST', 
        q_idx=q_idx, 
        scenario=current_scenario
    )

@app.route('/results')
def results():
    """
    Processes the aggregated scores and renders the analytical dashboard.
    """
    # Safety check: Ensure the user has completed all scenarios
    if 'u_v' not in session or len(session['u_v']) < 10:
        return redirect(url_for('home'))

    try:
        # Run the backend engine analysis
        assessment_results = psychometric_engine.process_assessment(session['u_v'])
        
        mastery_metrics = assessment_results.get('mastery_metrics', {})
        dimensional_variances = assessment_results.get('dimensional_variances', {})
        reliability_metrics = assessment_results.get('reliability_metrics', {})
        executive_report = assessment_results.get('executive_report', "")
        
        # Extract the dominant driver directly from the new engine output
        dominant_driver = reliability_metrics.get('dominant_trait', "Unknown")

        return render_template(
            'results.html',
            mastery_metrics=mastery_metrics,
            dimensional_variances=dimensional_variances,
            reliability_metrics=reliability_metrics,
            executive_report=executive_report,
            dominant_driver=dominant_driver
        )
    except Exception as e:
        # Graceful fallback if engine parsing fails
        print(f"Error processing results: {e}")
        return redirect(url_for('home'))

if __name__ == '__main__':
    # Run application
    app.run(host='0.0.0.0', port=5001, debug=True)