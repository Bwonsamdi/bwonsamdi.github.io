/*页面载入完成后，创建复制按钮*/ ! function(e, t, a) {
    /* code */
    var initCopyCode = function() {
        var copyHtml = '';
        copyHtml += '<button class="btn-copy button-primary button-box button-giant button-longshadow-right" data-clipboard-snippet="" >';
        copyHtml += '  <i class="fa fa-tag"></i>';
        copyHtml += '</button>';
        $(".highlight .code pre").before(copyHtml);
        new ClipboardJS('.btn-copy', {
            target: function(trigger) {
                return trigger.nextElementSibling;
            }
        });
    }
    initCopyCode();
}(window, document);