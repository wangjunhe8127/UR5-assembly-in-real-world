
(cl:in-package :asdf)

(defsystem "learning_communication-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "bianshi" :depends-on ("_package_bianshi"))
    (:file "_package_bianshi" :depends-on ("_package"))
    (:file "force_send" :depends-on ("_package_force_send"))
    (:file "_package_force_send" :depends-on ("_package"))
  ))