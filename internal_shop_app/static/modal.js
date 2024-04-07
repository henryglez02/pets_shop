function openDialog(dialogId, button) {
   const dialog = document.getElementById(dialogId);
   dialog.classList.remove('hidden');
   dialog.querySelector('input').focus();
    }
   
function closeDialog(button) {
   const dialog = button.closest('[role="dialog"]');
   dialog.classList.add('hidden');
    }
   
function replaceDialog(dialogId, newContent, closeButtonId) {
   const dialog = document.getElementById(dialogId);
   dialog.classList.add('hidden');
   if (closeButtonId) {
   document.getElementById(closeButtonId).style.display = 'none';
       }
    }
