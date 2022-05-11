// Auto-generated. Do not edit!

// (in-package learning_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class bianshi {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.g = null;
      this.fx = null;
      this.fy = null;
      this.fz = null;
      this.tx = null;
      this.ty = null;
      this.tz = null;
      this.x = null;
      this.y = null;
      this.px = null;
      this.py = null;
      this.pz = null;
    }
    else {
      if (initObj.hasOwnProperty('g')) {
        this.g = initObj.g
      }
      else {
        this.g = 0.0;
      }
      if (initObj.hasOwnProperty('fx')) {
        this.fx = initObj.fx
      }
      else {
        this.fx = 0.0;
      }
      if (initObj.hasOwnProperty('fy')) {
        this.fy = initObj.fy
      }
      else {
        this.fy = 0.0;
      }
      if (initObj.hasOwnProperty('fz')) {
        this.fz = initObj.fz
      }
      else {
        this.fz = 0.0;
      }
      if (initObj.hasOwnProperty('tx')) {
        this.tx = initObj.tx
      }
      else {
        this.tx = 0.0;
      }
      if (initObj.hasOwnProperty('ty')) {
        this.ty = initObj.ty
      }
      else {
        this.ty = 0.0;
      }
      if (initObj.hasOwnProperty('tz')) {
        this.tz = initObj.tz
      }
      else {
        this.tz = 0.0;
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('px')) {
        this.px = initObj.px
      }
      else {
        this.px = 0.0;
      }
      if (initObj.hasOwnProperty('py')) {
        this.py = initObj.py
      }
      else {
        this.py = 0.0;
      }
      if (initObj.hasOwnProperty('pz')) {
        this.pz = initObj.pz
      }
      else {
        this.pz = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type bianshi
    // Serialize message field [g]
    bufferOffset = _serializer.float64(obj.g, buffer, bufferOffset);
    // Serialize message field [fx]
    bufferOffset = _serializer.float64(obj.fx, buffer, bufferOffset);
    // Serialize message field [fy]
    bufferOffset = _serializer.float64(obj.fy, buffer, bufferOffset);
    // Serialize message field [fz]
    bufferOffset = _serializer.float64(obj.fz, buffer, bufferOffset);
    // Serialize message field [tx]
    bufferOffset = _serializer.float64(obj.tx, buffer, bufferOffset);
    // Serialize message field [ty]
    bufferOffset = _serializer.float64(obj.ty, buffer, bufferOffset);
    // Serialize message field [tz]
    bufferOffset = _serializer.float64(obj.tz, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = _serializer.float64(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float64(obj.y, buffer, bufferOffset);
    // Serialize message field [px]
    bufferOffset = _serializer.float64(obj.px, buffer, bufferOffset);
    // Serialize message field [py]
    bufferOffset = _serializer.float64(obj.py, buffer, bufferOffset);
    // Serialize message field [pz]
    bufferOffset = _serializer.float64(obj.pz, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type bianshi
    let len;
    let data = new bianshi(null);
    // Deserialize message field [g]
    data.g = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [fx]
    data.fx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [fy]
    data.fy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [fz]
    data.fz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [tx]
    data.tx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ty]
    data.ty = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [tz]
    data.tz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [px]
    data.px = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [py]
    data.py = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pz]
    data.pz = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 96;
  }

  static datatype() {
    // Returns string type for a message object
    return 'learning_communication/bianshi';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ef0f20add1753e4de26579161d3d529';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 g
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
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bianshi(null);
    if (msg.g !== undefined) {
      resolved.g = msg.g;
    }
    else {
      resolved.g = 0.0
    }

    if (msg.fx !== undefined) {
      resolved.fx = msg.fx;
    }
    else {
      resolved.fx = 0.0
    }

    if (msg.fy !== undefined) {
      resolved.fy = msg.fy;
    }
    else {
      resolved.fy = 0.0
    }

    if (msg.fz !== undefined) {
      resolved.fz = msg.fz;
    }
    else {
      resolved.fz = 0.0
    }

    if (msg.tx !== undefined) {
      resolved.tx = msg.tx;
    }
    else {
      resolved.tx = 0.0
    }

    if (msg.ty !== undefined) {
      resolved.ty = msg.ty;
    }
    else {
      resolved.ty = 0.0
    }

    if (msg.tz !== undefined) {
      resolved.tz = msg.tz;
    }
    else {
      resolved.tz = 0.0
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.px !== undefined) {
      resolved.px = msg.px;
    }
    else {
      resolved.px = 0.0
    }

    if (msg.py !== undefined) {
      resolved.py = msg.py;
    }
    else {
      resolved.py = 0.0
    }

    if (msg.pz !== undefined) {
      resolved.pz = msg.pz;
    }
    else {
      resolved.pz = 0.0
    }

    return resolved;
    }
};

module.exports = bianshi;
