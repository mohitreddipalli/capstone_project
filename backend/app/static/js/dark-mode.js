/* Dark Mode Toggle Functionality */

const DARK_MODE_KEY = 'darkMode';

/**
 * Initialize dark mode
 */
function initializeDarkMode() {
    const darkMode = localStorage.getItem(DARK_MODE_KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (darkMode !== null) {
        // User has set preference
        setDarkMode(darkMode === 'true');
    } else if (prefersDark) {
        // Use system preference
        setDarkMode(true);
    }
}

/**
 * Toggle dark mode
 */
function toggleDarkMode() {
    const isDarkMode = document.documentElement.getAttribute('data-bs-theme') === 'dark';
    setDarkMode(!isDarkMode);
}

/**
 * Set dark mode
 */
function setDarkMode(isDark) {
    const theme = isDark ? 'dark' : 'light';
    document.documentElement.setAttribute('data-bs-theme', theme);
    localStorage.setItem(DARK_MODE_KEY, isDark);
    
    // Update toggle button if it exists
    updateDarkModeToggle(isDark);
}

/**
 * Update dark mode toggle button
 */
function updateDarkModeToggle(isDark) {
    const toggle = document.querySelector('[onclick="toggleDarkMode()"]');
    if (toggle) {
        const icon = toggle.querySelector('i');
        if (icon) {
            if (isDark) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        }
    }
}

/**
 * Listen for system theme changes
 */
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (localStorage.getItem(DARK_MODE_KEY) === null) {
        setDarkMode(e.matches);
    }
});

// Initialize dark mode on page load
document.addEventListener('DOMContentLoaded', initializeDarkMode);

// Also initialize on window load as fallback
window.addEventListener('load', initializeDarkMode);

// Handle keyboard shortcut: Ctrl/Cmd + Shift + D for dark mode toggle
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'D') {
        e.preventDefault();
        toggleDarkMode();
    }
});
