Ext.define ('Webed.controller.SetTree', {
    extend: 'Ext.app.Controller',

    init: function () {
        this.control ({
            // TODO: Wire view events!
        });

        this.application.on ({
            synchronize: this.synchronize, scope: this
        });
    },

    synchronize: function () {
        console.debug ('[SetTreeCtrl.synchronize]', this);
    }
});
