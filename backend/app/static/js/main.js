/* Main JavaScript functionality */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize popovers
    initializePopovers();
    
    // Set up CSRF token for AJAX requests
    setupCSRFToken();
});

/**
 * Initialize Bootstrap tooltips
 */
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Initialize Bootstrap popovers
 */
function initializePopovers() {
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
}

/**
 * Set up CSRF token for AJAX requests
 */
function setupCSRFToken() {
    // If using Flask with CSRF protection, extract token from meta tag
    const csrfToken = document.querySelector('meta[name="csrf-token"]');
    if (csrfToken) {
        // Set up default headers for fetch
        const token = csrfToken.getAttribute('content');
        if (token) {
            window.csrfToken = token;
        }
    }
}

/**
 * Make AJAX GET request
 */
function ajaxGet(url, callback, errorCallback) {
    fetch(url, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    })
    .then(data => {
        if (callback) callback(data);
    })
    .catch(error => {
        console.error('AJAX GET error:', error);
        if (errorCallback) errorCallback(error);
    });
}

/**
 * Make AJAX POST request
 */
function ajaxPost(url, data, callback, errorCallback) {
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(data)
    };

    // Add CSRF token if available
    if (window.csrfToken) {
        options.headers['X-CSRFToken'] = window.csrfToken;
    }

    fetch(url, options)
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    })
    .then(data => {
        if (callback) callback(data);
    })
    .catch(error => {
        console.error('AJAX POST error:', error);
        if (errorCallback) errorCallback(error);
    });
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info', duration = 3000) {
    const toastHtml = `
        <div class="toast align-items-center text-bg-${type} border-0" role="alert">
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        </div>
    `;

    const toastContainer = document.getElementById('toastContainer');
    if (toastContainer) {
        toastContainer.insertAdjacentHTML('beforeend', toastHtml);
        const toastElement = toastContainer.lastElementChild;
        const toast = new bootstrap.Toast(toastElement);
        toast.show();

        // Remove element after toast is hidden
        toastElement.addEventListener('hidden.bs.toast', function() {
            toastElement.remove();
        });
    }
}

/**
 * Format currency
 */
function formatCurrency(amount, currency = 'USD') {
    const formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency
    });
    return formatter.format(amount);
}

/**
 * Format date
 */
function formatDate(date, format = 'MMM DD, YYYY') {
    const options = {
        year: 'numeric',
        month: format.includes('MMMM') ? 'long' : 'short',
        day: 'numeric'
    };
    return new Date(date).toLocaleDateString('en-US', options);
}

/**
 * Format time ago
 */
function timeAgo(date) {
    const seconds = Math.floor((new Date() - new Date(date)) / 1000);
    
    let interval = seconds / 31536000;
    if (interval > 1) return Math.floor(interval) + " years ago";
    
    interval = seconds / 2592000;
    if (interval > 1) return Math.floor(interval) + " months ago";
    
    interval = seconds / 86400;
    if (interval > 1) return Math.floor(interval) + " days ago";
    
    interval = seconds / 3600;
    if (interval > 1) return Math.floor(interval) + " hours ago";
    
    interval = seconds / 60;
    if (interval > 1) return Math.floor(interval) + " minutes ago";
    
    return Math.floor(seconds) + " seconds ago";
}

/**
 * Validate email
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validate password strength
 */
function getPasswordStrength(password) {
    let strength = 0;
    if (password.length >= 8) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[a-z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^A-Za-z0-9]/.test(password)) strength++;
    
    return strength;
}

/**
 * Get password strength badge
 */
function getPasswordStrengthBadge(password) {
    const strength = getPasswordStrength(password);
    const labels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong', 'Very Strong'];
    const colors = ['danger', 'danger', 'warning', 'info', 'success', 'success'];
    return `<span class="badge bg-${colors[strength]}">${labels[strength]}</span>`;
}

/**
 * Copy to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!', 'success');
    }).catch(err => {
        console.error('Failed to copy:', err);
        showToast('Failed to copy', 'danger');
    });
}

/**
 * Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

/**
 * Show loading spinner
 */
function showLoading(element) {
    const spinner = document.createElement('div');
    spinner.innerHTML = '<div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>';
    element.innerHTML = '';
    element.appendChild(spinner);
}

/**
 * Hide loading spinner
 */
function hideLoading(element) {
    const spinner = element.querySelector('.spinner-border');
    if (spinner) spinner.remove();
}

/**
 * Confirm before action
 */
function confirmAction(message) {
    return confirm(message || 'Are you sure?');
}

/**
 * Open modal
 */
function openModal(modalId) {
    const modal = new bootstrap.Modal(document.getElementById(modalId));
    modal.show();
}

/**
 * Close modal
 */
function closeModal(modalId) {
    const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
    if (modal) modal.hide();
}

// Create a toast container if it doesn't exist
window.addEventListener('load', function() {
    if (!document.getElementById('toastContainer')) {
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.style.position = 'fixed';
        container.style.top = '20px';
        container.style.right = '20px';
        container.style.zIndex = '9999';
        document.body.appendChild(container);
    }
});
