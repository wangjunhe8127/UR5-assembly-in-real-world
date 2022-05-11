;; Auto-generated. Do not edit!


(when (boundp 'learning_communication::bianshi)
  (if (not (find-package "LEARNING_COMMUNICATION"))
    (make-package "LEARNING_COMMUNICATION"))
  (shadow 'bianshi (find-package "LEARNING_COMMUNICATION")))
(unless (find-package "LEARNING_COMMUNICATION::BIANSHI")
  (make-package "LEARNING_COMMUNICATION::BIANSHI"))

(in-package "ROS")
;;//! \htmlinclude bianshi.msg.html


(defclass learning_communication::bianshi
  :super ros::object
  :slots (_g _fx _fy _fz _tx _ty _tz _x _y _px _py _pz ))

(defmethod learning_communication::bianshi
  (:init
   (&key
    ((:g __g) 0.0)
    ((:fx __fx) 0.0)
    ((:fy __fy) 0.0)
    ((:fz __fz) 0.0)
    ((:tx __tx) 0.0)
    ((:ty __ty) 0.0)
    ((:tz __tz) 0.0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:px __px) 0.0)
    ((:py __py) 0.0)
    ((:pz __pz) 0.0)
    )
   (send-super :init)
   (setq _g (float __g))
   (setq _fx (float __fx))
   (setq _fy (float __fy))
   (setq _fz (float __fz))
   (setq _tx (float __tx))
   (setq _ty (float __ty))
   (setq _tz (float __tz))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _px (float __px))
   (setq _py (float __py))
   (setq _pz (float __pz))
   self)
  (:g
   (&optional __g)
   (if __g (setq _g __g)) _g)
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
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:px
   (&optional __px)
   (if __px (setq _px __px)) _px)
  (:py
   (&optional __py)
   (if __py (setq _py __py)) _py)
  (:pz
   (&optional __pz)
   (if __pz (setq _pz __pz)) _pz)
  (:serialization-length
   ()
   (+
    ;; float64 _g
    8
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
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _px
    8
    ;; float64 _py
    8
    ;; float64 _pz
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _g
       (sys::poke _g (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _px
       (sys::poke _px (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _py
       (sys::poke _py (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pz
       (sys::poke _pz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _g
     (setq _g (sys::peek buf ptr- :double)) (incf ptr- 8)
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
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _px
     (setq _px (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _py
     (setq _py (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pz
     (setq _pz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get learning_communication::bianshi :md5sum-) "8ef0f20add1753e4de26579161d3d529")
(setf (get learning_communication::bianshi :datatype-) "learning_communication/bianshi")
(setf (get learning_communication::bianshi :definition-)
      "float64 g
float64 fx
float64 fy
float64 fz
float64 tx
float64 ty
float64 tz
float64 x
float64 y
float64 px
float64 py
float64 pz


")



(provide :learning_communication/bianshi "8ef0f20add1753e4de26579161d3d529")


