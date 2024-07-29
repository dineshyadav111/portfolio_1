function openPDF() {
    window.open('resume_canva.pdf', '_blank');
}
function animateSkills() {
    var skillsSection = document.getElementById('skills');
    // Remove the active class if it exists
    skillsSection.classList.remove('active');
    
    // Use setTimeout to allow the browser to reflow before adding the class again
    setTimeout(function() {
        skillsSection.classList.add('active');
    }, 50); // Slightly longer timeout to ensure animation class is reapplied
}