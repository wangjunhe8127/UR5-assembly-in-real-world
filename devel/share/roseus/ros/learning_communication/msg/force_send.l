;; Auto-generated. Do not edit!


(when (boundp 'learning_communication::force_send)
  (if (not (find-package "LEARNING_COMMUNICATION"))
    (make-package "LEARNING_COMMUNICATION"))
  (shadow 'force_send (find-package "LEARNING_COMMUNICATION")))
(unless (find-package "LEARNING_COMMUNICATION::FORCE_SEND")
  (make-package "LEARNING_COMMUNICATION::FORCE_SEND"))

(in-package "ROS")
;;//! \htmlinclude force_send.msg.html


(defclass learning_communication::force_send
  :super ros::object
  :slots (_fx _fy _fz _tx _ty _tz ))

(defmethod learning_communication::force_send
  (:init
   (&key
    ((:fx __fx) 0.0)
    ((:fy __fy) 0.0)
    ((:fz __fz) 0.0)
    ((:tx __tx) 0.0)
    ((:ty __ty) 0.0)
    ((:tz __tz) 0.0)
    )
   (send-super :init)
   (setq _fx (float __fx))
   (setq _fy (float __fy))
   (setq _fz (float __fz))
   (setq _tx (float __tx))
   (setq _ty (float __ty))
   (setq _tz (float __tz))
   self)
  (:fx
   (&optional __fx)
   (if __fx (setq _fx __fx)) _fx)
  (:fy
   (&optional __fy)
   (if __fy (setq _fy __fy)) _fy)
  (:fz
   (&optional __fz)
   (if __fz (setq _fz __fz)) _fz)
  (:tx
   (&optional __tx)
   (if __tx (setq _tx __tx)) _tx)
  (:ty
   (&optional __ty)
   (if __ty (setq _ty __ty)) _ty)
  (:tz
   (&optional __tz)
   (if __tz (setq _tz __tz)) _tz)
  (:serialization-length
   ()
   (+
    ;; float64 _fx
    8
    ;; float64 _fy
    8
    ;; float64 _fz
    8
    ;; float64 _tx
    8
    ;; float64 _ty
    8
    ;; float64 _tz
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _fx
       (sys::poke _fx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _fy
       (sys::poke _fy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _fz
       (sys::poke _fz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _tx
       (sys::poke _tx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ty
       (sys::poke _ty (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _tz
       (sys::poke _tz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _fx
     (setq _fx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _fy
     (setq _fy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _fz
     (setq _fz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _tx
     (setq _tx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ty
     (setq _ty (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _tz
     (setq _tz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get learning_communication::force_send :md5sum-) "e6da1f4bb463d64b2399f31589512a6f")
(setf (get learning_communication::force_send :datatype-) "learning_communication/force_send")
(setf (get learning_communication::force_send :definition-)
      "float64 fx
float64 fy
float64 fz
float64 tx
float64 ty
float64 tz


")



(provide :learning_communication/force_send "e6da1f4bb463d64b2399f31589512a6f")


