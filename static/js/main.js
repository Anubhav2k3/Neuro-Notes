// Main JavaScript functionality for Neuro Notes
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initializeModals();
    initializeMessages();
    initializeNoteCards();
    initializeAIFeatures();
    initializeDeleteFunctionality();
});

// Modal functionality
function initializeModals() {
    const helpBtn = document.getElementById('helpBtn');
    const helpModal = document.getElementById('helpModal');
    const aiResultModal = document.getElementById('aiResultModal');
    const deleteModal = document.getElementById('deleteModal');
    
    // Help modal
    if (helpBtn && helpModal) {
        helpBtn.addEventListener('click', () => {
            showModal(helpModal);
        });
    }
    
    // Close modals when clicking the close button or outside
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('close') || e.target.classList.contains('modal')) {
            hideAllModals();
        }
    });
    
    // Close modals with Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideAllModals();
        }
    });
}

// Show modal with animation
function showModal(modal) {
    modal.style.display = 'block';
    setTimeout(() => modal.classList.add('show'), 10);
}

// Hide all modals
function hideAllModals() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.style.display = 'none';
        modal.classList.remove('show');
    });
}

// Message functionality
function initializeMessages() {
    const messageCloses = document.querySelectorAll('.message-close');
    
    messageCloses.forEach(close => {
        close.addEventListener('click', () => {
            const message = close.parentElement;
            message.style.animation = 'slideOutUp 0.3s ease forwards';
            setTimeout(() => message.remove(), 300);
        });
    });
    
    // Auto-hide success messages after 5 seconds
    const successMessages = document.querySelectorAll('.message-success');
    successMessages.forEach(message => {
        setTimeout(() => {
            if (message.parentElement) {
                message.style.animation = 'slideOutUp 0.3s ease forwards';
                setTimeout(() => message.remove(), 300);
            }
        }, 5000);
    });
}

// Note cards functionality
function initializeNoteCards() {
    const showMoreBtns = document.querySelectorAll('.show-more-btn');
    
    showMoreBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.dataset.target;
            const preview = document.getElementById(`preview-${targetId}`);
            const full = document.getElementById(`full-${targetId}`);
            const showText = btn.querySelector('.show-text');
            const hideText = btn.querySelector('.hide-text');
            const icon = btn.querySelector('i');
            
            if (preview.style.display === 'none') {
                // Show preview, hide full
                preview.style.display = 'block';
                full.style.display = 'none';
                showText.style.display = 'inline';
                hideText.style.display = 'none';
                btn.classList.remove('expanded');
            } else {
                // Hide preview, show full
                preview.style.display = 'none';
                full.style.display = 'block';
                showText.style.display = 'none';
                hideText.style.display = 'inline';
                btn.classList.add('expanded');
            }
        });
    });
}

// AI Features functionality
function initializeAIFeatures() {
    const aiBtns = document.querySelectorAll('.ai-btn');
    const aiResultModal = document.getElementById('aiResultModal');
    const aiResultTitle = document.getElementById('aiResultTitle');
    const aiResultContent = document.getElementById('aiResultContent');
    const useAiResultBtn = document.getElementById('useAiResult');
    const closeAiResultBtn = document.getElementById('closeAiResult');
    const loadingOverlay = document.getElementById('loadingOverlay');
    
    let currentAiResult = '';
    let currentAction = '';
    
    aiBtns.forEach(btn => {
        btn.addEventListener('click', async () => {
            const action = btn.dataset.action;
            const contentTextarea = document.getElementById('content');
            const content = contentTextarea.value.trim();
            
            if (!content) {
                showNotification('Please enter some content first.', 'error');
                return;
            }
            
            currentAction = action;
            
            // Show loading overlay
            if (loadingOverlay) {
                loadingOverlay.style.display = 'block';
            }
            
            try {
                const result = await performAIAction(action, content);
                currentAiResult = result;
                
                // Update modal content
                if (aiResultTitle) {
                    aiResultTitle.innerHTML = `<i class="fas fa-robot"></i> ${getActionTitle(action)} Result`;
                }
                
                if (aiResultContent) {
                    aiResultContent.innerHTML = `<div class="ai-result-text">${formatAIResult(result)}</div>`;
                }
                
                // Show result modal
                if (aiResultModal) {
                    showModal(aiResultModal);
                }
                
            } catch (error) {
                console.error('AI Action Error:', error);
                showNotification('Failed to process AI request. Please try again.', 'error');
            } finally {
                // Hide loading overlay
                if (loadingOverlay) {
                    loadingOverlay.style.display = 'none';
                }
            }
        });
    });
    
    // Use AI result button
    if (useAiResultBtn) {
        useAiResultBtn.addEventListener('click', () => {
            const contentTextarea = document.getElementById('content');
            if (contentTextarea && currentAiResult) {
                // For grammar improvement, replace the content
                if (currentAction === 'improve_grammar') {
                    contentTextarea.value = currentAiResult;
                } else {
                    // For other actions, append or show in a way that makes sense
                    contentTextarea.value = currentAiResult;
                }
                
                // Trigger input event to update any character counts, etc.
                contentTextarea.dispatchEvent(new Event('input'));
                
                hideAllModals();
                showNotification('AI result applied successfully!', 'success');
            }
        });
    }
    
    // Close AI result button
    if (closeAiResultBtn) {
        closeAiResultBtn.addEventListener('click', () => {
            hideAllModals();
        });
    }
}

// Perform AI action via API
async function performAIAction(action, content) {
    const response = await fetch('/ai-action/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            action: action,
            content: content
        })
    });
    
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Network error occurred');
    }
    
    const data = await response.json();
    return data.result;
}

// Get CSRF token
function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    
    // Fallback: try to get from meta tag or hidden input
    const metaToken = document.querySelector('meta[name="csrf-token"]');
    if (metaToken) {
        return metaToken.getAttribute('content');
    }
    
    const hiddenToken = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (hiddenToken) {
        return hiddenToken.value;
    }
    
    return '';
}

// Get action title for display
function getActionTitle(action) {
    const titles = {
        'summarize': 'Summarize',
        'improve_grammar': 'Grammar Improvement',
        'translate': 'Hindi Translation',
        'analyze': 'Content Analysis'
    };
    return titles[action] || 'AI Processing';
}

// Format AI result for display
function formatAIResult(result) {
    // Convert line breaks to HTML and handle basic formatting
    return result
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>');
}

// Delete functionality
function initializeDeleteFunctionality() {
    const deleteButtons = document.querySelectorAll('.delete-note');
    const deleteModal = document.getElementById('deleteModal');
    const deleteForm = document.getElementById('deleteForm');
    const cancelDeleteBtn = document.getElementById('cancelDelete');
    
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const noteId = btn.dataset.noteId;
            
            if (deleteForm) {
                deleteForm.action = `/delete/${noteId}/`;
            }
            
            if (deleteModal) {
                showModal(deleteModal);
            }
        });
    });
    
    if (cancelDeleteBtn) {
        cancelDeleteBtn.addEventListener('click', () => {
            hideAllModals();
        });
    }
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `message message-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-triangle' : 'info-circle'}"></i>
        ${message}
        <button class="message-close">&times;</button>
    `;
    
    // Add to messages container or create one
    let messagesContainer = document.querySelector('.messages');
    if (!messagesContainer) {
        messagesContainer = document.createElement('div');
        messagesContainer.className = 'messages';
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
            mainContent.insertBefore(messagesContainer, mainContent.firstChild);
        }
    }
    
    messagesContainer.appendChild(notification);
    
    // Add close functionality
    const closeBtn = notification.querySelector('.message-close');
    closeBtn.addEventListener('click', () => {
        notification.style.animation = 'slideOutUp 0.3s ease forwards';
        setTimeout(() => notification.remove(), 300);
    });
    
    // Auto-hide after 5 seconds for success messages
    if (type === 'success') {
        setTimeout(() => {
            if (notification.parentElement) {
                notification.style.animation = 'slideOutUp 0.3s ease forwards';
                setTimeout(() => notification.remove(), 300);
            }
        }, 5000);
    }
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add some visual feedback for form submissions
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
            submitBtn.disabled = true;
            
            // Re-enable after a short delay (form will redirect anyway)
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 2000);
        }
    });
});

// Add slideOutUp animation for smooth message removal
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutUp {
        from { 
            opacity: 1; 
            transform: translateY(0); 
            max-height: 100px;
        }
        to { 
            opacity: 0; 
            transform: translateY(-30px); 
            max-height: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;
        }
    }
    
    .ai-result-text {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid var(--accent-color);
        line-height: 1.6;
        white-space: pre-wrap;
        max-height: 400px;
        overflow-y: auto;
    }
`;
document.head.appendChild(style);
