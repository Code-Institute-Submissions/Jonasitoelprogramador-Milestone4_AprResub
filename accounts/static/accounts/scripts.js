/*var signup_1 = document.getElementbyId("signup-step-1");
signup_1.addEventListener("click", next_input)

function next_input() {
    This needs to hold the submit until the next form has been filled out
    var register_form = document.getElementbyId("register_form");
    register_form.innerHTML = 
`<div class="form-group">
<div>{% if post_paramater == 'host' %}
    <label for="nationality_first">Nationality</label>
    {{profile_form.nationality}} 
{% else %}  
    <label for="nationality_first">First Language</label>
    {{profile_form.first_language}}
{% endif %}</div>   
</div>
<div class="form-group">
{% if post_paramater == 'host' %}
    <label for="first_language_desired">First Language</label>
    {{profile_form.first_language}}  
{% else %} 
    <label for="first_language_desired">Desired Language</label>
    {{profile_form.desired_language}} 
{% endif %}     
</div>
<div class="form-group">
{% if post_paramater == 'host' %}
    <label for="location_experience">Location</label>
    {{profile_form.location}}  
{% else %} 
    <label for="location_experience">Work Experience Category</label>
    {{profile_form.work_experience_category}}
{% endif %}  
</div>
<div class="form-group">
{% if profile_form.work_experience %}
<label for="name">Work Experience</label>
{{profile_form.work_experience}} 
{% endif %}  
</div>
<div class="form-group form-button">
<input type="submit" name="signup-step-2" id="signup-step-2" class="form-submit" value="Register"/>
</div>`
}