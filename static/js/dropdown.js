// Wait for the webpage to load
document.addEventListener('DOMContentLoaded', () => {

    // Select dropdown-triggers
    const dropdowns = document.querySelectorAll('.dropdown');
    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger');

    //Closes the dropdowns
    const closeAllDropdowns = () => {
        dropdowns.forEach(dropdown => {
            dropdown.classList.remove('is-active');
        });
    };

    //If anything on the page is clicked
    dropdownTriggers.forEach(trigger => {
        trigger.addEventListener('click', (event) => {

            // Prevents event from going to parent or child elements
            event.stopPropagation();

            // Looks for what was clicked
            const dropdown = trigger.closest('.dropdown');

            // If this dropdown is already active, close it
            if (dropdown.classList.contains('is-active')) {
                dropdown.classList.remove('is-active');
            } else {
                // Close all other dropdowns, then open this one
                closeAllDropdowns();
                dropdown.classList.add('is-active');
            }
        });
    });

    // Listens for clicks on the entire document
    document.addEventListener('click', () => {
        // Clicking anywhere will close the dropdown
        closeAllDropdowns();
    });
});